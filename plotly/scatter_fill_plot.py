# DAVIDRVU - 2019

# pip freeze | findstr seaborn              # PARA REVISAR VERSION DE SEABORN
# conda install -c anaconda seaborn=0.9.0   # PARA INSTALAR NUEVA VERSION DE SEABORN

from plotly.graph_objs import Scatter, Figure, Layout, Scattergl
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from sklearn.metrics import mean_absolute_error
import datetime
import numpy as np
import sys

numdays       = 5
multiplicador = 100

base = datetime.date.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

data_true_lim = [3000,3000,3000,3000,3000]
data_true1    = [1000, 1500, 2000, 1000, 1500]
#data_pred1    = [1100, 1400, 2100, 900, 1600]


line_size     = 3
trace1 = Scatter(
    x=date_list,
    y=data_true1,
    line = dict(width=line_size),
    fill='tozeroy', # tozeroy
    mode='none', # lines+markers+text
    showlegend=True,
    name = 'Subestimado', # Style name/legend entry with html tags
)
trace2 = Scatter(
    x=date_list,
    y=data_true_lim,
    line = dict(width=line_size),
    fill='tonexty', # tozeroy
    mode='none', # lines+markers+text
    showlegend=True,
    name = 'Sobrestimado'
)
trace3 = Scatter(
    x=date_list,
    y=data_true1,
    line = dict(width=line_size, color='rgba(0, 0, 152, 1)'),
    mode='lines+markers', # lines+markers+text
    showlegend=True,
    name = 'True data', # Style name/legend entry with html tags
)

#add_scatter(x=xs[[0,-1]], y=[11,11], fill='tonexty')

data = [trace1, trace2, trace3]

layout = {
    'title': "Forecast",
    'xaxis': {
        'title': 'Dates',
    },
    'yaxis': {
        'title': 'Units',
    },
    'showlegend': True,
    #'plot_bgcolor':'rgb(233,0,0)'
}

fig = dict(data = data, layout = layout)
plot(fig, filename="test.html")



