import math
import matplotlib.pyplot as plt
import pandas as pd
from GR86.chassis.taskcenter.tushare_task import TushareTask
import logging

import itertools

from GR86.engine.analysis.utils import get_percent, format_money

template = {
    'total_assets': "一、资产总计",
    'total_cur_assets': "流动资产合计",
    'total_nca': "非流动资产合计",
    'total_liab': "二、负债合计",
    'total_hldr_eqy_inc_min_int': "三、 股东权益总计",
}

row_labels_keys = [new_value for new_value in template.keys()]
row_labels = [new_value for new_value in template.values()]



def percent_data(obj):
    return_obj = {}
    for item in row_labels_keys:
        if obj.get(item) is None:
            return_obj[item] = '/'
        elif math.isnan(obj.get(item)):
            return_obj[item] = '/'
        else:
            return_obj[item] = '{:,.2f}%'.format(get_percent(obj, item, "total_assets"))
    return return_obj


def load_data(idx_and_item):
    index, item = idx_and_item

    if (index % 2) == 0:
        return format_money(item, row_labels_keys)
    else:
        return percent_data(item)



def get_data_and_col_labels(cursor):
    copy = list(cursor)
    double_list = list(itertools.chain(*zip(copy, copy)))
    col_label = ['金额 {0}'.format(double_list[x].get('ts_code')) if x % 2 == 0 else '占比' for x in
                 range(len(double_list))]
    data = list(map(load_data, enumerate(double_list)))
    df = pd.DataFrame(data,
                      columns=row_labels_keys)
    df = df.transpose()
    return {
        'data': df.values.tolist(),
        'col_label': col_label
    }


def get_view(cursor):
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    copy_cursor = list(cursor)
    table_amount = math.ceil(len(copy_cursor) / 5)

    plt.figure(figsize=(20, 14))

    for i in range(table_amount):
        show_data = copy_cursor[i * 5: i * 5 + 5]
        plt.table(cellText=get_data_and_col_labels(show_data).get('data'),
                  colLabels=get_data_and_col_labels(show_data).get('col_label'),
                  rowLabels=row_labels,
                  loc='center',
                  cellLoc='center',
                  rowLoc='center')
        plt.subplot(table_amount, 1, i + 1)
        plt.axis('off')

    plt.show()
