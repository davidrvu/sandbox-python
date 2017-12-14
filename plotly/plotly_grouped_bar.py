from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Bar
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

def plotly_grouped_bar(allTrace, filename, title_in):
    print("\n----> START plotly_grouped_bar")
    layout = {
                'barmode': 'group',
                'showlegend': True,
                'title': title_in,
                'yaxis': {
                    'autorange': 'reversed',
                }
            }
    fig = dict(data = allTrace, layout = layout)
    print("PLOTLY_GROUPED_BAR filename = " + filename)
    plot(fig, filename=filename)

    print("----> END plotly_grouped_bar\n") 