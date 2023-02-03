from GR86.chassis.taskcenter.tushare_task import TushareTask
from GR86.chassis.spider.tushare import Tushare
from GR86.chassis.taskcenter.work_type import WorkType
import queue
import logging
from threading import Thread, Event
import sys
import time

event = Event()


class Producer(Tushare, Thread):
    def __init__(self, thread_id, fetch_data_queue, save_to_mongo_queue, work_type):
        Tushare.__init__(self)
        Thread.__init__(self)
        self.work_type = work_type
        self.thread_id = thread_id
        self.fetch_data_queue = fetch_data_queue
        self.save_to_mongo_queue = save_to_mongo_queue

    def get_work_info(self, item):
        start_date = "20170101"
        end_date = "20221229"
        if self.work_type == WorkType.BALANCE_SHEET:
            data = Tushare.get_balance_sheet(self, ts_code=item, start_date=start_date, end_date=end_date)
        elif self.work_type == WorkType.INCOME_STATEMENT:
            data = Tushare.get_income_statement(self, ts_code=item, start_date=start_date, end_date=end_date)
        elif self.work_type == WorkType.CASH_FLOW:
            data = Tushare.get_cash_flow(self, ts_code=item, start_date=start_date, end_date=end_date)
        return data

    def run(self):
        while not self.fetch_data_queue.empty():
            try:
                item = self.fetch_data_queue.get()
                time.sleep(0.1)
                data = self.get_work_info(item)

                logging.info('爬取数据: 获取 股票 %s ， 数据长度 %s' % (item, data.size))
                save_to_mongo_data = {
                    "work_type": self.work_type,
                    "data": data
                }
                self.fetch_data_queue.task_done()
                self.save_to_mongo_queue.put(save_to_mongo_data)
                event.set()
            except queue.Empty:
                logging.info('任务完成' % (item, self.thread_id))
            if item is None:
                logging.info('下载完成')
                break


class Consumer(Thread, TushareTask):
    def __init__(self, thread_id, fetch_data_queue, save_to_mongo_queue):

        Thread.__init__(self)
        TushareTask.__init__(self)
        self.thread_id = thread_id
        self.fetch_data_queue = fetch_data_queue
        self.save_to_mongo_queue = save_to_mongo_queue

    def start_work(self, item):
        if item.get("work_type") == WorkType.BALANCE_SHEET:
            TushareTask.save_balance_sheet_mongodb(self, sheet=item.get('data').to_dict("records"))
        elif item.get("work_type") == WorkType.INCOME_STATEMENT:
            TushareTask.save_income_statement_to_mongodb(self, sheet=item.get('data').to_dict("records"))
        elif item.get("work_type") == WorkType.CASH_FLOW:
            TushareTask.save_cash_flow_to_mongodb(self, sheet=item.get('data').to_dict("records"))

    def run(self):
        while True:
            if self.save_to_mongo_queue.empty():
                Event().wait(0.5)
                if self.fetch_data_queue.empty():
                    logging.info('Consumer notify : no item to consume')
                    break

            item = self.save_to_mongo_queue.get()
            if item.get('data').size > 0:
                self.start_work(item)
            logging.info('存入mongodb: 数据长度 %s ， %s' % (item.get('data').size, self.thread_id))
            self.save_to_mongo_queue.task_done()


def do_task():
    f = FinialStatementTask()
    fetch_balance_queue = queue.Queue(maxsize=0)
    fetch_cash_flow_queue = queue.Queue(maxsize=0)
    fetch_income_queue = queue.Queue(maxsize=0)
    save_to_mongo_queue = queue.Queue(maxsize=0)
    list_stock = f.init_queue()
    logging.info(list_stock)
    for item in list_stock:
        fetch_balance_queue.put(item)
        fetch_cash_flow_queue.put(item)
        fetch_income_queue.put(item)

    p1 = Producer('Producer-0001', fetch_balance_queue, save_to_mongo_queue, WorkType.BALANCE_SHEET)
    p2 = Producer('Producer-0002', fetch_cash_flow_queue, save_to_mongo_queue, WorkType.CASH_FLOW)
    p3 = Producer('Producer-0003', fetch_income_queue, save_to_mongo_queue, WorkType.INCOME_STATEMENT)
    t1 = Consumer('Consumer-0001', fetch_balance_queue, save_to_mongo_queue)
    t2 = Consumer('Consumer-0002', fetch_balance_queue, save_to_mongo_queue)
    try:

        p1.start()
        p2.start()
        p3.start()
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        p1.join()
        p2.join()
        p3.join()
    except KeyboardInterrupt:
        sys.exit(1)


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
        return list(map(lambda x: x.get("symbol"), cursor))

    def get_stock(self, symbol):
        cursor = self.collection_stock_list.find({
            "symbol": symbol
        })
        return cursor
