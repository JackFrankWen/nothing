from enum import Enum


class WorkType(Enum):
    BALANCE_SHEET = 'BALANCE_SHEET'
    INCOME_STATEMENT = 'INCOME_STATEMENT'
    CASH_FLOW = 'CASH_FLOW'
    FIN_INDICATORS = 'financial_indicators'
    FIN_AUDIT_OPINION = 'financial_audit_opinion'
