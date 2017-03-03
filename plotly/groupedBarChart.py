from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Bar
import numpy as np 

trace1 = Bar(    
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)

trace2 = Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]

layout = Layout(
    barmode='group'
)

fig = dict(data = data, layout = layout)
plot(fig, filename='groupedBarChart.html', auto_open=True)