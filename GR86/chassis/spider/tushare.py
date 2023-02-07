import tushare as ts
from GR86.chassis.spider.base import spider


class Tushare(spider):
    def __init__(self):
        # ts.set_token('18d06f6b9689112d57777972863107f8f53ffde39f7e7d21089cfbd7')

        self.pro = ts.pro_api('18d06f6b9689112d57777972863107f8f53ffde39f7e7d21089cfbd7')

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
                               # fields=[
                               #     'ts_code',
                               #     'ann_date',
                               #     'f_ann_date',
                               #     'end_date',
                               #     'report_type',
                               #     'comp_type',
                               #     'basic_eps',
                               #     'diluted_eps',
                               #     'other_bus_cost',
                               #     'operate_profit',
                               #     'non_oper_income',
                               #     'non_oper_exp',
                               #     'nca_disploss',
                               #     'total_profit',
                               #     'income_tax',
                               #     'n_income',
                               #     'n_income_attr_p',
                               #     'minority_gain',
                               #     'oth_compr_income',
                               #     't_compr_income',
                               #     'compr_inc_attr_p',
                               #     'compr_inc_attr_m_s',
                               #     'ebit',
                               #     'ebitda',
                               #     'insurance_exp',
                               #     'undist_profit',
                               #     'distable_profit',
                               #     'rd_exp',
                               #     'fin_exp_int_exp',
                               #     'fin_exp_int_inc',
                               #     'transfer_surplus_rese',
                               #     'transfer_housing_imprest',
                               #     'transfer_oth',
                               #     'adj_lossgain',
                               #     'withdra_legal_surplus',
                               #     'withdra_legal_pubfund',
                               #     'withdra_biz_devfund',
                               #     'withdra_rese_fund',
                               #     'withdra_oth_ersu',
                               #     'workers_welfare',
                               #     'distr_profit_shrhder',
                               #     'prfshare_payable_dvd',
                               #     'comshare_payable_dvd',
                               #     'capit_comstock_div',
                               #     'net_after_nr_lp_correct',
                               #     'credit_impa_loss',
                               #     'net_expo_hedging_benefits',
                               #     'oth_impair_loss_assets',
                               #     'total_opcost',
                               #     'amodcost_fin_assets',
                               #     'oth_income',
                               #     'asset_disp_income',
                               #     'continued_net_profit',
                               #     'end_net_profit',
                               # ]
                               )

    def get_balance_sheet(self, ts_code, start_date, end_date):
        """

        :param ts_code:
        :param start_date:
        :param end_date:
        :return:
        """
        code = self.transform(ts_code)

        return self.pro.balancesheet(ts_code=code, start_date=start_date, end_date=end_date,
                                     # fields=[
                                     #     # asset = liability + equity
                                     #     "ts_code",
                                     #     "f_ann_date",
                                     #     "report_type",  # 报表类型
                                     #     # 左边
                                     #     "total_assets",  # 资产总计
                                     #     "total_nca",  # 非流动资产合计
                                     #     "total_cur_assets",  # 流动资产合计
                                     #     "fix_assets_total",  # 固定资产(合计)(元)
                                     #     # 右边
                                     #
                                     #     "total_liab_hldr_eqy",  # 负债及股东权益总计
                                     #     "total_hldr_eqy_inc_min_int",  # 股东权益合计(含少数股东权益)
                                     #     "total_liab",  # 负债合计
                                     #     "total_cur_liab",  # 流动负债合计
                                     #     "total_ncl",  # 流动负债合计
                                     #     "total_liab_hldr_eqy",  # 负债及股东权益总计
                                     #
                                     # ]
                                     )

    def get_stock_basic(self):
        return self.pro.stock_basic(exchange='', list_status='L',fields='ts_code,symbol,name,area,industry,list_date,exchange')

    def get_daily_basic(self, trade_date):
        return self.pro.daily_basic(ts_code='', trade_date=trade_date,
                                    # fields=["ts_code",
                                    #         "trade_date",
                                    #         "turnover_rate",
                                    #         "volume_ratio",
                                    #         "pe",
                                    #         "pb",
                                    #         ]
                                    )

