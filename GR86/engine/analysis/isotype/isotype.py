import logging
import math


from GR86.chassis.taskcenter.tushare_task import TushareTask
from GR86.engine.analysis.isotype.income_statement import get_view, get_percent


def net_profit_over_ten_percent(obj):
    return get_percent(obj,  'n_income', "total_revenue") > 15


def get_data_by_rule(cursor):
    return filter(net_profit_over_ten_percent, list(cursor))


def run():
    n = TushareTask()

    search_list = n.collection_stock_list.find({"industry": '水泥'})
    arr = list(map(lambda x: x.get("ts_code"), search_list))
    cursor = n.collection_income_statement.find({"ts_code": {
        "$in": arr
    }, "end_type": '4', "end_date":  "20191231"})
    cursor2 = n.collection_balance_sheet.find({"ts_code": {
        "$in": arr
    }, "end_type": '4', "end_date":  "20191231"})

    get_view(get_data_by_rule(cursor))
