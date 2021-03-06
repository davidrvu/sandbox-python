# DAVIDRVU 2018

# SOURCE: https://stackoverflow.com/questions/28161244/how-to-create-two-y-axes-streaming-plotly

from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis
import datetime
import numpy as np
import plotly.plotly as py # plotly library
import sys
import time

def main():
    print("RECEIVER AND PLOT")

    # Plot.ly credentials and stream tokens
    username                 = 'davidrvu'
    api_key                  = 'hOQ0feXyuUxZ0WtrhUgt'
    stream_token_temperature = 'aghuvyozmm'
    stream_token_humidity    = '5mfgh2l9jl'

    print("py.sign_in ...")
    py.sign_in(username, api_key)
    print("py.sign_in DONE!")

    trace_temperature = Scatter(
        x=[],
        y=[],
       stream=Stream(
            token=stream_token_temperature
        ),
        yaxis='y',
        name="temperature",
        mode="lines+markers",
    )

    trace_humidity = Scatter(
        x=[],
        y=[],
        stream=Stream(
            token=stream_token_humidity
        ),
        yaxis='y2',
        name="humidity",
        mode="lines+markers",
    )

    layout = Layout(
        title='Plotly streaming test',
        yaxis=YAxis(
            title='Celcius'
        ),
        yaxis2=YAxis(
            title='%',
            side='right',
            overlaying="y"
        )
    )

    data = Data([trace_temperature, trace_humidity])
    fig = Figure(data=data, layout=layout)

    print(py.plot(fig, filename='Plotly streaming test'))

if __name__ == "__main__":
    main()