from GR86.chassis.taskcenter.tushare_task import TushareTask
from GR86.chassis.spider.tushare import Tushare
import sys
import queue
import logging
from threading import Thread,Event,Condition
import time
import random
event = Event()

class Producer(Tushare, Thread):
    def __init__(self, thread_id, fetch_data_queue, save_to_mongo_queue):
        Tushare.__init__(self)
        Thread.__init__(self)

        self.thread_id = thread_id
        self.fetch_data_queue = fetch_data_queue
        self.save_to_mongo_queue = save_to_mongo_queue


    def run(self):
        while not self.fetch_data_queue.empty():
            try:
                item = self.fetch_data_queue.get()
                time.sleep(1)
                data = Tushare.get_balance_sheet(self, ts_code=item)
                logging.info('爬取数据: 获取 股票 %s ， 数据长度 %s' % (item, data.size))
                self.fetch_data_queue.task_done()
                self.save_to_mongo_queue.put(data)
                event.set()
            except queue.Empty:
                logging.info('任务完成' % (item, self.thread_id))
            if item is None:
                logging.info('下载完成')
                break






class Consumer(Thread,TushareTask):
    def __init__(self, thread_id, fetch_data_queue, save_to_mongo_queue):
        Thread.__init__(self)
        TushareTask.__init__(self)
        self.thread_id = thread_id
        self.fetch_data_queue = fetch_data_queue
        self.save_to_mongo_queue = save_to_mongo_queue

    def run(self):
        while True:
            if self.save_to_mongo_queue.empty():
                Event().wait(1)
                if self.fetch_data_queue.empty():
                    logging.info('Consumer notify : no item to consume')
                    break

            item = self.save_to_mongo_queue.get()
            if item.size > 0:
                TushareTask.save_balance_sheet_mongodb(self, sheet=item.to_dict("records"))
            logging.info('存入mongodb: 数据长度 %s ， %s' % (item.size, self.thread_id))
            self.save_to_mongo_queue.task_done()





def do_balance_sheet_task():
    f = FinialStatementTask()
    fetch_data_queue = queue.Queue(maxsize=0)
    save_to_mongo_queue = queue.Queue(maxsize=0)
    list_stock = f.init_queue()
    logging.info(list_stock)
    t = Tushare()

    logging.info( t.get_balance_sheet('000001'))
    logging.info( len(list_stock))
    logging.info('长度%s  ' % (len(list_stock)))

    for item in list_stock:
        fetch_data_queue.put(item)
    t1 = Producer('Producer-0001', fetch_data_queue, save_to_mongo_queue)
    t2 = Consumer('Consumer-0002', fetch_data_queue, save_to_mongo_queue)
    t3 = Consumer('Consumer-0003', fetch_data_queue, save_to_mongo_queue)
    try:

        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
    except KeyboardInterrupt:
        sys.exit(1)


    # for record in list:
        # f.save_balance_sheet_mongodb(record)



class FinialStatementTask(TushareTask):

    def __init__(self):
        super().__init__()

    def init_queue(self):
        # SSE上交所 SZSE深交所 BSE北交所
        cursor = self.collection_stock_list.find({
            "$or": [{
                "exchange": "SSE"
            }, {
                "exchange": "SZSE"
            }]
        })
        return list(map(lambda x: x.get("symbol"),cursor))



