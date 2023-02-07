def format_money(obj, income_statement_col):
    """

    :param obj:
    :param income_statement_col:
    :return: string '111,111'
    """
    new_obj = {}
    for item in income_statement_col:
        if obj.get(item) is None:
            new_obj[item] = '/'
        else:
            new_obj[item] = '{:,.0f}'.format(obj.get(item))
    return new_obj


def get_percent(obj, first, sec):
    """

    :param obj:
    :param first: 12.22
    :param sec: 100
    :return: int 12.22
    """
    return int(obj.get(first)) / int(obj.get(sec)) * 100

def get_col_labels_and_col_keys(tempalte):
    return {

    }