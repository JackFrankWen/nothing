import logging
from GR86.chassis.taskcenter.base import Task

log = logging.getLogger(__name__)

db_name = "test"
collection_stock_list = "stock_list"
collection_balance_sheet = "balance_sheet"
collection_cash_flow = "cash_flow"
collection_income_statement = "income_statement"
view_pe = "daily_basic_view_pe"
view_pb = "daily_basic_view_pe"


class TushareTask(Task):

    def __init__(self):
        super().__init__()
        self.db_name = db_name

        self.db = self.m.get_client()[self.db_name]
        self.collection_stock_list = self.db[collection_stock_list]
        self.collection_balance_sheet = self.db[collection_balance_sheet]
        self.collection_cash_flow = self.db[collection_cash_flow]
        self.collection_income_statement = self.db[collection_income_statement]
        self.daily_basic = self.db["daily_basic"]

        # self.save_basic()
        # self.save_balance_sheet()
        # self.save_daily_basic()

        # self.db.command({
        #     "create": "daily_basic_view_pe",
        #     "viewOn": "daily_basic",
        #     "pipeline": [
        #         {
        #             "$sort": {"pe": -1},
        #             "$gte": {"pe": 0},
        #
        #         }
        #     ]
        # })
        # self.db.command({
        #     "create": "daily_basic_view_pb",
        #     "viewOn": "daily_basic",
        #     "pipeline": [
        #         {
        #             "$gte": {"pb": 0},
        #             "$sort": {"pb": -1}
        #         }
        #     ]
        # })

    def check(self, collection):
        if len(list(collection.find())) > 0:
            return True
        else:
            return False

    def save_cash_flow_to_mongodb(self, sheet):
        self.collection_cash_flow.insert_many(sheet)
        logging.info(sheet)

    def get_and_save_cash_flow_to_mongodb(self, ts_code):
        sheet = self.t.get_cash_flow(ts_code=ts_code)
        self.collection_cash_flow.insert_many(sheet.to_dict("records"))
        logging.info(sheet)

    def save_income_statement_to_mongodb(self, sheet):
        self.collection_income_statement.insert_many(sheet)
        logging.info(sheet)

    def get_and_save_income_statement_to_mongodb(self, ts_code):
        sheet = self.t.get_income_statement(ts_code=ts_code)
        self.collection_income_statement.insert_many(sheet.to_dict("records"))
        logging.info(sheet)

    def save_balance_sheet_mongodb(self, sheet):
        self.collection_balance_sheet.insert_many(sheet)
        logging.info(sheet)

    def get_and_save_balance_sheet_mongodb(self, ts_code):
        sheet = self.t.get_balance_sheet(ts_code=ts_code)
        self.collection_balance_sheet.insert_many(sheet.to_dict("records"))
        logging.info(sheet)

    def get_and_save_stock_list_to_mongodb(self):
        basic = self.t.get_stock_basic()
        self.collection_stock_list.insert_many(basic.to_dict("records"))
