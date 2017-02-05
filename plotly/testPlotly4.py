from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl

line_size = 3


#shapesD = dict(
#    # Line Vertical
#    type = 'line',
#    x0 = 1,
#    y0 = 0,
#    x1 = 1,
#    y1 = 15,
#    line = dict(
#        color = 'rgb(255, 0, 0)',
#        width = 3,
#        dash = 'dashdot',
#    )
#)

#layout = Layout(
#    title='testPlotly3',
#    xaxis=dict(
#        title='EJE X',
#        titlefont=dict(
#            family='Courier New, monospace',
#            size=18,
#            color='#7f7f7f'
#        )
#    ),
#    yaxis=dict(
#        title='EJE Y',
#        titlefont=dict(
#            family='Courier New, monospace',
#            size=18,
#            color='#7f7f7f'
#        )
#    ),
#    shapes = shapesD, 
#    showlegend=True
#)

layout = {
    'title': 'testPlotly3', 
    'xaxis': {
        'title': 'EJE X',
        'titlefont' : {
            'family': 'Courier New, monospace',
            'size': 18,
            'color': '#7f7f7f'
        },       
        #'range': [0, 7]
    },
    'yaxis': {
        'title': 'EJE Y',
        'titlefont' : {
            'family': 'Courier New, monospace',
            'size': 18,
            'color': '#7f7f7f'
        #'range': [0, 2.5]
        },
    },
    'shapes': [
        # Line Vertical
        {
            'type': 'line',
            'x0': '2016-12-06 22:23:00',
            'y0': 0,
            'x1': '2016-12-06 22:23:00',
            'y1': 30,
            'line': {
                'color': 'rgb(255, 0, 0)',
                'width': 5,
                'dash': 'dashdot',
            },
        }
    ],
    'showlegend': True
}

# OJO, se puden usar x axis de tipo datetime
#datetime(year=2013, month=10, day=04, hour=23, minute=46)
# EJ: x = [datetime(year=2013, month=10, day=04), datetime(year=2013, month=11, day=05)

trace1 = Scatter(
    #x=[1, 2, 3, 4, 5, 
    #   6, 7, 8, 9, 10,
    #   11, 12, 13, 14, 15],
    x=['2015-04-04 22:23:00', 
       '2015-05-04 22:23:00', 
       '2015-06-04 22:23:00',
       '2015-09-02 22:22:00',
       '2015-09-02 22:23:00',
       '2015-09-03 22:23:00',
       '2015-09-04 22:23:00',
       '2016-05-04 22:23:00',
       '2016-06-04 22:23:00',
       '2016-07-04 22:23:00',
       '2016-08-04 22:23:00',
       '2016-09-04 22:23:00',
       '2016-10-04 22:23:00',
       '2016-11-04 22:23:00',
       '2016-12-04 22:23:00'
       ],
    y=[10, 20, 21, 15, 12,
       11, 15, 23, 15, 13,
       10, 15, None, 24, 10],
    text=['Text 1', 'Text 2', 'Text 3','Text 4', 'Text 5',
    	  'Text 6', 'Text 7', 'Text 8','Text 9', 'Text 10',
    	  'Text 11', 'Text 12', 'Text 13','Text 14', 'Text 15'
    	],
    line = dict(width=line_size),
    mode='lines+markers', # lines+markers+text
    connectgaps=False,
    showlegend=True,
    name = '<b>EN NEGRITA - NO </b> Gaps', # Style name/legend entry with html tags
)

trace2 = Scatter(
    x=[1.5, 2.5, 3.5, 4.5, 5.5,
       6.5, 7.5, 8.5, 9.5, 10.5,
       11.5, 12.5, 13.5, 14.5, 15.5],
    y=[5, 15, None, 10, 5,
       0, 10, None, 15, 5,
       5, 10, 20, 15, 5],
    line = dict(width=line_size),
    showlegend=True,
    name = 'Gaps',
)

trace3 = Scatter(
    x=[1.5, 2.5, 3.5, 4.5, 5.5,
       6.5, 7.5, 8.5, 9.5, 10.5,
       11.5, 12.5, 13.5, 14.5, 15.5],
    y=[2, None, None, 8, 6,
       1, 5, 12, 14, None,
       5.5, 10.25, 2, 3, 6],
    name = 'Gaps',
    line = dict(width=line_size),
    showlegend=True,
)

#data = [trace1, trace2, trace3] # TODOTODO: PONER SUBPLOT CON LEGEND SEPARADA
data = [trace1]
fig = dict(data = data, layout = layout)
plot(fig, filename='test4.html')