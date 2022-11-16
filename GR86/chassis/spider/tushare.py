import tushare as ts
from GR86.chassis.spider.base import spider

start_date = "20180101"
end_date = "20180730"

class Tushare(spider):
    def __init__(self):
        # ts.set_token('18d06f6b9689112d57777972863107f8f53ffde39f7e7d21089cfbd7')

        self.pro = ts.pro_api('546c968a0b21a389e604ec18621a75a693abcb82f8c8699d42ab774f')

    def get(self):
        return self.pro.daily(ts_code='000001.SZ', start_date=start_date, end_date='20180718')

    def get_cash_flow(self, ts_code):
        """
        现金流表
        :param ts_code:
        :return:
        """
        code = self.transform(ts_code)
        return self.pro.cashflow(ts_code=code, start_date=start_date, end_date='20180730')

    def get_income_statement(self, ts_code):
        """
        利润表
        :param ts_code:
        :return:
        """
        code = self.transform(ts_code)
        return self.pro.income(ts_code=code, start_date=start_date, end_date='20180730',
                               fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps')

    def get_balance_sheet(self, ts_code):
        """
        资产表
        :param ts_code:
        :return:
        """
        code = self.transform(ts_code)
        return self.pro.balancesheet(ts_code=code, start_date='20170101', end_date='20221231',
                                     end_type="4",
                                     fields=[
                                         "ts_code",
                                         "f_ann_date",
                                         "report_type",  # 报表类型
                                         # 左边
                                         "total_nca",  # 非流动资产合计
                                         "total_cur_assets",  # 流动资产合计
                                         # "fix_assets_total",  # 固定资产(合计)(元)
                                         # 右边
                                         "total_hldr_eqy_inc_min_int",  # 股东权益合计(含少数股东权益)
                                         "total_liab",  # 负债合计
                                         "total_liab_hldr_eqy",  # 负债及股东权益总计

                                     ])

    def get_stock_basic(self):
        return self.pro.stock_basic(**{
            "ts_code": "",
            "name": "",
            "exchange": "",
            "market": "",
            "is_hs": "",
            "list_status": "L",
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "symbol",
            "name",
            "area",
            "industry",
            "market",
            "list_date",
            "exchange",
            "delist_date"
        ])

    def get_daily_basic(self, trade_date):
        return self.pro.daily_basic(ts_code='', trade_date=trade_date,
                                    fields=["ts_code",
                                            "trade_date",
                                            "turnover_rate",
                                            "volume_ratio",
                                            "pe",
                                            "pb",
                                            ]
                                    )

    def get_stock_company(self):
        return self.pro.stock_company(**{
            "ts_code": "300459.SZ\t",
            "exchange": "",
            "status": "",
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "exchange",
            "chairman",
            "manager",
            "secretary",
            "reg_capital",
            "setup_date",
            "province",
            "city",
            "website",
            "email",
            "employees"
        ])
