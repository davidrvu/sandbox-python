# DAVIDRVU 2018

from plotly.graph_objs import Scatter, Figure, Layout, Scattergl
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import os
import pandas as pd
import time

def perf_read_csv_zip(file_name):
    print("perf_read_csv_zip: file_name = " + str(file_name))
    start_time = time.time()
    dataframe  = pd.read_csv(file_name, compression="zip")
    end_time   = time.time()
    total_time = end_time - start_time
    print("        total_time = " + str(round(total_time,4)) + "[s]. para perf_read_csv_zip de archivo " + str(file_name))
    del dataframe
    return total_time

def perf_read_csv(file_name):
    print("perf_read_csv: file_name = " + str(file_name))
    start_time = time.time()
    dataframe  = pd.read_csv(file_name)
    end_time   = time.time()
    total_time = end_time - start_time
    print("        total_time = " + str(round(total_time,4)) + "[s]. para perf_read_csv de archivo " + str(file_name))
    del dataframe
    return total_time

def file_size_MB(file_name):
    size_bytes = float(os.path.getsize(file_name))
    size_mb    = float((size_bytes/1024.0)/1024.0)
    print("        size_mb = " + str(size_mb) + "[MB]")
    return size_mb

def main():
    print("="*60)
    print("    PERFORMANCE  pd.read_csv pd.read_csv(ZIP) - BY DAVIDRVU")
    print("="*60)

    y_time_zip  = [0]*6
    y_time      = [0]*6
    x_file_size = [0]*6

    y_time_zip[0]  = perf_read_csv_zip("C:/datasets/bimbo_inventory_demand/town_state.csv.zip")
    y_time[0]      = perf_read_csv("C:/datasets/bimbo_inventory_demand/town_state.csv")
    x_file_size[0] = file_size_MB("C:/datasets/bimbo_inventory_demand/town_state.csv")

    y_time_zip[1]  = perf_read_csv_zip("C:/datasets/bimbo_inventory_demand/producto_tabla.csv.zip")
    y_time[1]      = perf_read_csv("C:/datasets/bimbo_inventory_demand/producto_tabla.csv")
    x_file_size[1] = file_size_MB("C:/datasets/bimbo_inventory_demand/producto_tabla.csv")

    y_time_zip[2]  = perf_read_csv_zip("C:/datasets/bimbo_inventory_demand/cliente_tabla.csv.zip")
    y_time[2]      = perf_read_csv("C:/datasets/bimbo_inventory_demand/cliente_tabla.csv")
    x_file_size[2] = file_size_MB("C:/datasets/bimbo_inventory_demand/cliente_tabla.csv")

    y_time_zip[3]  = perf_read_csv_zip("C:/datasets/bimbo_inventory_demand/sample_submission.csv.zip")
    y_time[3]      = perf_read_csv("C:/datasets/bimbo_inventory_demand/sample_submission.csv")
    x_file_size[3] = file_size_MB("C:/datasets/bimbo_inventory_demand/sample_submission.csv")

    y_time_zip[4]  = perf_read_csv_zip("C:/datasets/bimbo_inventory_demand/test.csv.zip")
    y_time[4]      = perf_read_csv("C:/datasets/bimbo_inventory_demand/test.csv")
    x_file_size[4] = file_size_MB("C:/datasets/bimbo_inventory_demand/test.csv")

    y_time_zip[5]  = perf_read_csv_zip("C:/datasets/bimbo_inventory_demand/train.csv.zip")
    y_time[5]      = perf_read_csv("C:/datasets/bimbo_inventory_demand/train.csv")
    x_file_size[5] = file_size_MB("C:/datasets/bimbo_inventory_demand/train.csv")


    print(y_time_zip)
    print(y_time)
    print(x_file_size)

    trace_zip = Scatter(
        x=x_file_size,
        y=y_time_zip,
        mode='markers+lines',
        name='Time read_csv ZIPPED',
        line=dict(
            color='red'
        )
    )
    trace = Scatter(
        x=x_file_size,
        y=y_time,
        mode='markers+lines',
        name='Time read_csv',
        line=dict(
            color='blue'
        )
    )

    data = [trace_zip, trace]
    layout = Layout(
        title="Pandas read_csv performance (ZIP files)",
        xaxis=dict(
            title='File size [MB]',
            titlefont=dict(
                family='Arial, sans-serif',
                size=18,
                color='black'
            ),
            autorange=True,
            showgrid=True,
        ),
        yaxis=dict(
            title='read_csv time [seg]',
            titlefont=dict(
                family='Arial, sans-serif',
                size=18,
                color='black'
            ),
            autorange=True,
            showgrid=True,
        )
    )
    fig = Figure(data=data, layout=layout)

    plot(fig, filename='pandas_read_csv_perf.html')


    print("Done!")

if __name__ == "__main__":
    main()