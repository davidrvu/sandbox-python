# DAVIDRVU - 2017

from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Bar
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

def plotly_grouped_bar(allTrace, filename, title_in, **kwargs):
    print("\n----> START plotly_grouped_bar")

    margin_left = kwargs.get('margin_left', 100)         # default value
    xaxis_title = kwargs.get('xaxis_title', "Frequency") # default value 
    yaxis_title = kwargs.get('yaxis_title', "Type")      # default value 

    layout = {
                'barmode': 'group',
                'showlegend': True,
                'title': title_in,
                'yaxis': {
                    'title': yaxis_title,
                    'autorange': 'reversed',
                },
                'xaxis': {
                    'title': xaxis_title,
                },
                'margin': {
                    'l': margin_left,
                }
            }
    fig = dict(data = allTrace, layout = layout)
    print("PLOTLY_GROUPED_BAR filename = " + filename)
    plot(fig, filename=filename)

    print("----> END plotly_grouped_bar\n") 