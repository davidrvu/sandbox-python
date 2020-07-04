# DAVIDRVU - 2020

# OJO: Para guardar plotly como imagen, se debe instalar:
#      conda install -c plotly plotly-orca==1.2.1 psutil requests

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl
import datetime

def main():

    layout = {
        'title': 'Título ' + str(datetime.datetime.now()) , 
        'title_x':0.5,
        'xaxis': {
            'title': 'EJE X'
        },
        'yaxis': {
            'title': 'EJE Y'
        },
        'showlegend': True,
        'template': "plotly_dark"
    }

    trace1 = Scatter(
        x=['2015-04-04 22:23:00', '2015-05-04 22:23:00', '2015-06-04 22:23:00', '2015-09-02 22:22:00', '2015-09-02 22:23:00', '2015-09-03 22:23:00', '2015-09-04 22:23:00', '2016-05-04 22:23:00'],
        y=[10, 20, 21, 15, 12, 11, 15, 23],
        line = dict(width=2),
        mode='lines+markers', # lines+markers+text
        connectgaps=False,
        showlegend=True,
        name = '<b>EN NEGRITA </b> Style', # Style name/legend entry with html tags           
    )

    trace2 = Scatter(
        x=['2015-04-05 00:00:00', '2015-05-06 00:00:00', '2015-06-10 00:00:00', '2016-11-10 00:00:00'],
        y=[8, 25, 14, 20],
        line = dict(width=2),
        mode='lines+markers', # lines+markers+text
        connectgaps=False,
        showlegend=True,
        name = 'trace2', # Style name/legend entry with html tags           
    )

    data = [trace1, trace2]
    fig = Figure(data = data, layout = layout)
    #plot(fig, filename='plotly_dark.html', auto_open=False)
    fig.write_image("plotly_dark.png", width=1600, height=900, scale=1)

    print("DONE!")

if __name__ == "__main__":
    main()