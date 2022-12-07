from GR86.chassis.taskcenter.tushare_task import TushareTask
from GR86.chassis.spider.tushare import Tushare
import queue
import logging
from threading import Thread
import time
import random


class Producer(Thread, Tushare):
    def __init__(self, thread_id, fetch_data_queue, save_to_mongo_queue):
        Thread.__init__(self)
        super(Tushare, self).__init__()

        self.thread_id = thread_id
        self.fetch_data_queue = fetch_data_queue
        self.save_to_mongo_queue = save_to_mongo_queue


    def run(self):
        while True:
            try:
                item = self.fetch_data_queue.get(timeout=0.5)
                # data = self.get_balance_sheet(item)
                logging.info('Producer notify : %d popped from queue by %s' % (item, self.thread_id))
                self.fetch_data_queue.task_done()
                self.save_to_mongo_queue.put(item)
            except queue.Empty:
                print()
            if item is None:
                break
        logging.info('下载完成')






class Consumer(Thread):
    def __init__(self, thread_id, queue):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            logging.info('Consumer notify : %d popped from queue by %s' % (item, self.thread_id))
            print('Consumer notify : %d popped from queue by %s' % (item, self.name))
            self.queue.task_done()





def do_balance_sheet_task():
    f = FinialStatementTask()
    fetch_data_queue = queue.Queue(maxsize=0)
    save_to_mongo_queue = queue.Queue(maxsize=0)
    list_stock = f.init_queue()
    logging.info(list_stock)
    t = Tushare()
    for item in list_stock:
        fetch_data_queue.put(item)
    t1 = Producer('0001', fetch_data_queue, save_to_mongo_queue)
    t2 = Consumer('0002', save_to_mongo_queue)
    t3 = Consumer('0003', save_to_mongo_queue)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


    # for record in list:
        # f.save_balance_sheet_mongodb(record)



class FinialStatementTask(TushareTask):

    def __init__(self):
        super().__init__()

    def init_queue(self):
        cursor = self.collection_stock_list.find({
            "$or": [{
                "exchange": "SSE"
            }, {
                "exchange": "SZSE"
            }]
        })
        return list(map(lambda x: x.get("symbol"),cursor))

    def save_balance_sheet_mongodb(self, code):
        self.save_balance_sheet_mongodb(code)


