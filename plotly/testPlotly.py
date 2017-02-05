from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

from plotly.graph_objs import Scatter, Figure, Layout, Scattergl

plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], filename='testScatter.html')

#plot([Scattergl(x=[1, 2, 3], y=[3, 1, 6])], filename='testScatterGl.html')