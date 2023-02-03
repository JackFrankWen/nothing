import matplotlib.pyplot as plt
from GR86.engine.analysis.isotype.income_statement import get_col_labels, get_row_labels, get_data_and_col_labels

def run():
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


    # 行名
    row = get_row_labels()
    # 表格里面的具体值
    data = get_data_and_col_labels()
    plt.figure(figsize=(20, 8))
    tab = plt.table(cellText=data.get('data'),
                    colLabels=data.get('col_label'),
                    rowLabels=row,
                    loc='center',
                    cellLoc='center',
                    rowLoc='center')
    tab.scale(1, 2)
    plt.axis('off')
    plt.show()
