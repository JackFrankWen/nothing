import tushare as ts
from GR86.chassis.spider.base import spider


class Tushare(spider):
    def __init__(self):
        # ts.set_token('18d06f6b9689112d57777972863107f8f53ffde39f7e7d21089cfbd7')

        self.pro = ts.pro_api('9fee1265156331df83250fbf6ae2c1034bf1f3693cc93e650dbe7cb6')
        # self.pro = ts.pro_api('18d06f6b9689112d57777972863107f8f53ffde39f7e7d21089cfbd7')

    def get_cash_flow(self, ts_code, start_date, end_date):
        """

        :param ts_code:
        :param start_date:
        :param end_date:
        :return:
        """
        code = self.transform(ts_code)
        return self.pro.cashflow(ts_code=code, start_date=start_date, end_date=end_date)

    def get_income_statement(self, ts_code, start_date, end_date):
        """
        利润表
        :param ts_code:
        :param start_date:
        :param end_date:
        :return:
        """
        code = self.transform(ts_code)
        return self.pro.income(ts_code=code, start_date=start_date, end_date=end_date,
                               )

    def get_audit_opinion(self, ts_code, start_date, end_date):
        """
        审计意见
         :param ts_code:
         :param start_date:
         :param end_date:
         :return:
         """
        code = self.transform(ts_code)
        return self.pro.fina_audit(ts_code=code, start_date=start_date, end_date=end_date)

    def get_financial_indicators(self, ts_code, start_date, end_date):
        """
        财务指标数据
        :param ts_code:
        :param start_date:
        :param end_date:
        :return:
        """
        code = self.transform(ts_code)
        return self.pro.fina_audit(ts_code=code, start_date=start_date, end_date=end_date)

    def get_main_business_info(self, ts_code):
        """
        主营业务
        :param ts_code:
        :return:
        """
        return self.pro.fina_mainbz(ts_code=ts_code, type='P')

    def get_balance_sheet(self, ts_code, start_date, end_date):
        """

        :param   ts_code:
        :param start_date:
        :param end_date:
        :return:
        """
        code = self.transform(ts_code)

        return self.pro.balancesheet(ts_code=code, start_date=start_date, end_date=end_date)

    def get_stock_basic(self):
        return self.pro.stock_basic(exchange='', list_status='L',fields='ts_code,symbol,name,area,industry,list_date,exchange')


    def get_daily_basic(self, trade_date):
        return self.pro.daily_basic(ts_code='', trade_date=trade_date,)

