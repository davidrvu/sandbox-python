# DAVIDRVU 2018

from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

def main():
    print("RECEIVER AND PLOT")

    stream_token = 'AAABBB'

    trace1 = Scatter(
        x=[],
        y=[],
        stream=dict(
            token=stream_token,
            maxpoints=200
        )
    )

    layout = Layout(
        title='Streaming Data'
    )

    data = [trace1]

    fig = dict(data=data, layout=layout)

    plot(fig, filename='streaming_plot.html')

if __name__ == "__main__":
    main()