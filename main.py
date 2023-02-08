from GR86.chassis.taskcenter.financial_statement_task import do_task
from GR86.chassis.taskcenter.tushare_task import TushareTask
from GR86.engine.analysis.isotype.isotype import run
import logging
logging.getLogger().setLevel(logging.DEBUG)


def main():
    # run()
    # t = TushareTask()
    # t.get_and_save_stock_list_to_mongodb()
    #
    # f = FinialStatementTask()
    # do_balance_sheet_task()
    # t.save_stock_list_to_mongodb()
    # t.save_balance_sheet_mongodb("000651")
    # t.save_cash_flow_to_mongodb("000651")
    # t.save_income_statement_to_mongodb("000651")
    do_task()



if __name__ == '__main__':
    main()
