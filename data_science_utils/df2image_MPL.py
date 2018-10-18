# DAVIDRVU - 2018
# FUENTE: https://stackoverflow.com/questions/26678467/export-a-pandas-dataframe-as-a-table-image/26681726

from printDeb import printDeb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import six
import subprocess
import sys

def df2image_MPL(debug, data, filename_output, col_width, row_height, font_size, header_color, row_colors, edge_color, bbox=[0, 0, 1, 1], header_columns=0, ax=None, **kwargs):
    printDeb(debug, "\n----> START " + str(sys._getframe().f_code.co_name) )
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)
    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    fig = ax.get_figure()
    fig.savefig(filename_output)
    printDeb(debug, "----> END " + str(sys._getframe().f_code.co_name) + "\n")

def main():
    ########################################
    ## PARAMETERS
    ########################################
    df_in = pd.DataFrame()
    df_in['date'] = ['2016-04-01', '2020-04-02', '2016-04-03', '2017-09-09']
    df_in['calories'] = [2200, 2100, 1500, 1000]
    df_in['sleep hours'] = [2200, 2100, 1500, 1000]
    df_in['gym'] = [True, False, False, False]
    df_in['gym2'] = [12, 10, 5, 1]

    debug           = 0
    filename_output = "output.png"
    col_width       = 1.6
    row_height      = 0.5
    font_size       = 12
    header_color    = "#21830E" #'#40466e'
    row_colors      = ['#f1f1f2', 'w']
    edge_color      = 'w'
    ########################################

    df2image_MPL(debug, df_in, filename_output, col_width, row_height, font_size, header_color, row_colors, edge_color)

    subprocess.Popen(filename_output, shell=True)

if __name__ == "__main__":
    main()