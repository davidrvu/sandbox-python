import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Surface, Layout, Scene

init_notebook_mode()

x, y = np.mgrid[-2*np.pi:2*np.pi:300j, -2:2:300j]

surface = Surface(
    x=x, y=y, z=-np.cos(x)+y**2/2
)

#iplot([surface])
plot([surface], filename='test1.html')


layout = Layout(scene=Scene(xaxis=dict(range=[-1,1])))
plot(dict(data=[surface], layout=layout), filename='test2.html')