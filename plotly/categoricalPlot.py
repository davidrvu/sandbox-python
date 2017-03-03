from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl
import numpy as np 


def dataFromStringToNum(yDataOriginal, Ycategorical, YcategoricalLen):
  output = []
  for i in range(0, len(yDataOriginal)):
    if yDataOriginal[i] is None:
      output.append(None)
    else:
      for j in range(0, YcategoricalLen):
        if(yDataOriginal[i] == Ycategorical[j]):
          output.append(j+1)
          break
  return output

line_size = 3

Ycategorical = ['R', 'U', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
print "Ycategorical = "
print Ycategorical

YcategoricalLen = len(Ycategorical)
print "YcategoricalLen = " + str(YcategoricalLen)

Yvalue = list(np.linspace(1, YcategoricalLen, YcategoricalLen, endpoint=True).astype(int))
print "Yvalue = "
print Yvalue

layout = {
    'title': 'categoricalPlot', 
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
        'title': 'EJE Y CATEGORICO',
        #'ticklen': 10,
        #'tickwidth': 10,
        'tickmode': "array",
        'tickvals': Yvalue,
        'ticktext': Ycategorical,
        'showticklabels': True,
        'titlefont' : {
            'family': 'Courier New, monospace',
            'size': 18,
            'color': '#7f7f7f'
        #'range': [0, 2.5]
        },
    },
    'showlegend': True
}

yDataOriginal = ["U","1","5","8","2","1","7","R","4","1","2","4",None,"2","6"]
print "yDataOriginal = "
print yDataOriginal
yDataNumeric = dataFromStringToNum(yDataOriginal, Ycategorical, YcategoricalLen)
print "yDataNumeric = "
print yDataNumeric

trace1 = Scatter(
    x=['2015-04-04 22:23:00', 
       '2015-05-04 22:23:00', 
       '2015-06-04 22:23:00',
       '2015-07-02 22:22:00',
       '2015-08-02 22:23:00',
       '2015-09-03 22:23:00',
       '2015-10-04 22:23:00',
       '2016-05-04 22:23:00',
       '2016-06-04 22:23:00',
       '2016-07-04 22:23:00',
       '2016-08-04 22:23:00',
       '2016-09-04 22:23:00',
       '2016-10-04 22:23:00',
       '2016-11-04 22:23:00',
       '2016-12-04 22:23:00'
       ],
    #y=[10, 20, 21, 15, 12,
    #   11, 15, 23, 15, 13,
    #   10, 15, None, 24, 10],
    y=yDataNumeric,       
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

data = [trace1]
fig = dict(data = data, layout = layout)
plot(fig, filename='categoricalPlot.html', auto_open=True)

## TODOTODO: revisar eje Y -> no aparece el tick "1"