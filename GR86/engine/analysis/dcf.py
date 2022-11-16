# DCF Model
# https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-model-training-free-guide/
# https://www.investopedia.com/investing/what-is-a-cash-flow-statement/
#
# the Net Present Value (NPV)

# DCF Valuation
# NPV of Forecast
# Terminal Value
# NPV of Terminal Value
# Total Enterprise value
# discount rate
# WACC weighted average cost of capital
# WACC = D÷(E+D) x Rd x (1-t) + E÷(E+D) x Re
# E = 總股東權益
# D = 總負債
# Re = 股權成本 = 無風險報酬 + β（期望市場報酬 - 無風險報酬）
# Rd = 債權成本 = 利息費用 ×（1-t）÷ 總負債
# t = 公司稅率

# What Is DCF Used For?
# A discounted cash flow valuation is used to determine if an investment is worthwhile in the long run.


# FCFF=税后经营净利润+折旧摊销-资本性支出-经营营运资本增加
# 税后经营利润：税后经营净利润=净利润+利息支出（筹资过程科目）-税
# 资本性支出=末期固定资产-初期固定资产+折旧+末期无形资产-初期无形资产+摊销

#
# The discounted cash flow (DCF) analysis is a method in finance of valuing a security, project, company,
# or asset using the concepts of the time value of money.
# Discounted cash flow analysis is widely used in investment finance, real estate development,
# corporate financial management and patent valuation.
# It was used in industry as early as the 1700s or 1800s, widely discussed in financial economics in the 1960s,
# and became widely used in U.S. courts in the 1980s and 1990s.
#
#  经营性营运资本增加=末期经营性营运资本-初期经营经营性营运资本
# Net Operating Profit After Tax
class DCFModel:

    def __init__(self):
        self.FCFF = ''

    def get_net_profit_after_tax(self):
        pass

    def get(self):
        pass