import math
import matplotlib.pyplot as plt
import pandas as pd
from GR86.chassis.taskcenter.tushare_task import TushareTask
import logging

import itertools

income_statement_col = [
    'total_revenue',
    'total_cogs',
    # 'oper_cost',
    # 'int_exp',
    # 'sell_exp',
    # 'admin_exp',
    # 'fin_exp',
    'operate_profit',
    'total_profit',
    "n_income",
]


def get_row_labels():
    row = [
        "一、 营业总收入",
        "二、 营业总成本",
        # " 减:营业成本",
        # " 减:利息支出",
        # " 减:销售费用",
        # " 减:管理费用",
        # " 减:财务费用",
        "三、 营业利润",  # 营业总收入—营业总成本+投资收益+公允价值变动收益—资产减值损失—信用减值损失
        "四、利润总额",
        "五、净利润",
    ]
    return row


def format_money(obj):
    new_obj = {}
    for item in income_statement_col:
        if obj.get(item) is None:
            new_obj[item] = '/'
        else:
            new_obj[item] = '{:,.0f}'.format(obj.get(item))
    return new_obj


def get_percent(obj, first, sec):
    return int(obj.get(first)) / int(obj.get(sec)) * 100


def percent_data(obj):
    return_obj = {
        'total_revenue': "100%"
    }
    for item in income_statement_col:
        if item != 'total_revenue':
            if obj.get(item) is None:

                return_obj[item] = '/'
            elif math.isnan(obj.get(item)):
                return_obj[item] = '/'

            else:
                return_obj[item] = '{:,.2f}%'.format(get_percent(obj, item, "total_revenue"))
    return return_obj


def load_data(idx_and_item):
    index, item = idx_and_item

    if (index % 2) == 0:
        return format_money(item)
    else:
        return percent_data(item)


def get_data_and_col_labels(cursor):
    return load_data_and_col_labels(cursor)

def load_data_and_col_labels(cursor):
    copy = list(cursor)
    double_list = list(itertools.chain(*zip(copy, copy)))
    col_label = ['金额 {0}'.format(double_list[x].get('ts_code')) if x % 2 == 0 else '占比' for x in
                 range(len(double_list))]
    data = list(map(load_data, enumerate(double_list)))
    df = pd.DataFrame(data,
                      columns=income_statement_col)
    df = df.transpose()
    return {
        'data': df.values.tolist(),
        'col_label': col_label
    }


def get_view(cursor):
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    row = get_row_labels()

    copy_cursor = list(cursor)
    table_amount = math.ceil(len(copy_cursor) / 5)

    plt.figure(figsize=(20, 14))

    for i in range(table_amount):
        show_data = copy_cursor[i * 5: i * 5 + 5]
        logging.info(show_data)
        plt.table(cellText=get_data_and_col_labels(show_data).get('data'),
                  colLabels=get_data_and_col_labels(show_data).get('col_label'),
                  rowLabels=row,
                  loc='center',
                  cellLoc='center',
                  rowLoc='center')
        plt.subplot(table_amount, 1, i + 1)
        plt.axis('off')

    plt.show()
