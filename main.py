from GR86.chassis.spider.tushare import Tushare
from GR86.chassis.taskcenter.tushare_task import TushareTask
import logging
from GR86.chassis.spider.joinquant import demo
logging.getLogger().setLevel(logging.DEBUG)


def main():
    # t = TushareTask()
    #
    # t.save_stock_list_to_mongodb()
    # t.save_balance_sheet_mongodb("000651")
    # t.save_cash_flow_to_mongodb("000651")
    # t.save_income_statement_to_mongodb("000651")
    demo()

if __name__ == '__main__':
    main()
