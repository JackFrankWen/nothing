from itertools import chain

import pandas as pd
from GR86.chassis.taskcenter.tushare_task import TushareTask
import logging

import itertools

income_statement_col = ['total_revenue', 'total_cogs', 'operate_profit', 'total_profit', "n_income"]


def get_row_labels():
    row = [
        "一、 营业总收入",
        "二、 营业总成本",
        "三、 营业利润",  # 营业总收入—营业总成本+投资收益+公允价值变动收益—资产减值损失—信用减值损失
        "四、利润总额",
        "五、净利润",
    ]
    return row


def get_col_labels():
    col = ["金额", "占比"]
    return col


def formate_money(obj):
    new_obj = {}
    for item in income_statement_col:
        new_obj[item] = '{:,.0f}'.format(obj.get(item))
    return new_obj


def get_percent(obj, first, sec):
    return int(obj.get(first)) / int(obj.get(sec)) * 100


def percent_data(obj):
    return_obj = {'total_cogs': '{:,.2f}%'.format(get_percent(obj, "total_cogs", "total_revenue")),
                  'operate_profit': '{:,.2f}%'.format(get_percent(obj, "operate_profit", "total_revenue")),
                  'total_profit': '{:,.2f}%'.format(get_percent(obj, "total_profit", "total_revenue")),
                  'n_income': '{:,.2f}%'.format(get_percent(obj, "n_income", "total_revenue")), 'total_revenue': "100%"}
    return return_obj


def updata(idx_and_item):
    index, item = idx_and_item

    if (index % 2) == 0:
        return formate_money(item)
    else:
        return percent_data(item)


def get_data_and_col_labels():
    n = TushareTask()
    cursor = n.collection_income_statement.find({"ts_code": '600585.SH', "end_type": '4', })
    copy = list(cursor)
    double_list = list(itertools.chain(*zip(copy, copy)))
    col_label = ['金额' if x % 2 == 0 else '占比' for x in range(len(double_list))]
    data = list(map(updata, enumerate(double_list)))
    df = pd.DataFrame(data,
                      columns=income_statement_col)
    df = df.transpose()
    return {
        'data': df.values.tolist(),
        'col_label': col_label
    }
