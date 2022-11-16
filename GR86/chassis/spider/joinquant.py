import jqdatasdk as jq

import logging

# aa 为你自己的帐号， bb 为你自己的密码
jq.auth('13918191207', 'Join$446034')


def demo():
    data = jq.normalize_code(["000001"])
    ino = get_income_statement(data)
    logging.debug(ino)


def get_all_etf():
    return jq.get_all_securities(['etf'])


def get_cash_flow_statement(security):
    return jq.get_history_fundamentals(security=security, fields=[jq.cash_flow], watch_date=None, stat_date=None,
                                       count=99, interval='1q', stat_by_year=False)


def get_income_statement(security):
    return jq.get_history_fundamentals(security=security, fields=[jq.income], watch_date=None, stat_date="2005q1",
                                       count=99, interval='1q', stat_by_year=False)


def get_balance_sheet(security):
    return jq.get_history_fundamentals(security=security, fields=[jq.balance], watch_date=None, stat_date=None,
                                       count=99, interval='1q', stat_by_year=False)


def get_trade_days(start_date=None, end_date=None, count=None):
    """

    start_date: 开始日期, 与 count 二选一, 不可同时使用. str/[datetime.date]/[datetime.datetime] 对象
    end_date: 结束日期, str/[datetime.date]/[datetime.datetime] 对象, 默认为 datetime.date.today()
    count: 数量, 与 start_date 二选一, 不可同时使用, 必须大于 0. 表示取 end_date 往前的 count 个交易日，包含 end_date 当天。
    :return:
    """
    return jq.get_trade_days(start_date=start_date, end_date=end_date, count=count)
