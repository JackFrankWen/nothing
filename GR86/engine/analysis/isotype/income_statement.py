import math
import matplotlib.pyplot as plt
import pandas as pd
from GR86.chassis.taskcenter.tushare_task import TushareTask
import logging

import itertools

from GR86.engine.analysis.utils import format_money, get_percent
from GR86.engine.analysis.view.table_view import get_tabulate_view

template = {
    'total_revenue':  "一、 营业总收入",
    'total_cogs': "二、 营业总成本",
    'operate_profit':  "三、 营业利润",  # 营业总收入—营业总成本+投资收益+公允价值变动收益—资产减值损失—信用减值损失
    'total_profit': "四、利润总额",
    "n_income":  "五、净利润",

}


row_labels_keys = [new_value for new_value in template.keys()]
row_labels = [new_value for new_value in template.values()]


def percent_data(obj):
    return_obj = {
        'total_revenue': "100%"
    }
    for item in row_labels_keys:
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
        return format_money(item, row_labels_keys)
    else:
        return percent_data(item)


def get_data_and_col_labels(cursor):
    copy = list(cursor)
    double_list = list(itertools.chain(*zip(copy, copy)))
    col_label = ['金额 {0}'.format(double_list[x].get('ts_code')) if x % 2 == 0 else '占比' for x in
                 range(len(double_list))]
    data = list(map(load_data, enumerate(double_list)))
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    df = pd.DataFrame(data,
                      index=col_label,
                      columns=row_labels_keys)
    df = df.transpose()
    df = pd.DataFrame(df.values.tolist(),
                      index=row_labels,
                      columns=col_label)
    logging.info(f"\n{df.to_markdown()}",)
    return df


def get_view(cursor):
    copy_cursor = list(cursor)

    get_tabulate_view(get_data_and_col_labels(copy_cursor), 'income_statement')

