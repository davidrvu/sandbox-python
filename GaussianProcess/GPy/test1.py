# pip install gpy
# HELP GPy    > http://nbviewer.jupyter.org/github/SheffieldML/notebook/blob/master/GPy/basic_gp.ipynb
# HELP PLOTLY > https://plot.ly/python/line-charts/
import GPy
import numpy as np
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Line
from IPython.display import display


#################################################
## Gaussian process regression tutorial
#################################################
## 1-dimensional model

def main():
    GPy.plotting.change_plotting_library('plotly')

    numPuntos = 100

    X = np.random.uniform(-3.,3.,(numPuntos,1))
    Y = np.sin(X) + np.random.randn(numPuntos,1)*0.05 #Y include some noise.

    #The first step is to define the covariance kernel we want to use for the model.
    kernel = GPy.kern.RBF(input_dim=1, variance=1., lengthscale=1.)

    #The parameter input_dim stands for the dimension of the input space. 
    #The parameters variance and lengthscale are optional, and default to 1. 
    #Many other kernels are implemented, type GPy.kern.<tab> to see a list

    #The inputs required for building the model are the observations and the kernel:
    m = GPy.models.GPRegression(X,Y,kernel)


    ###########
    m.optimize(messages=True)
    m.optimize_restarts(num_restarts = 10)
    ###########
    fig = m.plot()

    ###print fig
    # Points Scatter
    yData = list(fig[0]['data'][1]['y'])
    xData = list(fig[0]['data'][1]['x'])

    # Mean
    yMean = list(fig[0]['data'][0]['y'])
    xMean = list(fig[0]['data'][0]['x'])

    # Limite inferior
    yInf  = list(fig[0]['data'][2]['y'])
    xInf  = list(fig[0]['data'][2]['x'])

    # Limite superior
    ySup  = list(fig[0]['data'][3]['y'])
    xSup  = list(fig[0]['data'][3]['x'])

    # Create a trace
    traceData = Scatter(
        x    = xData,
        y    = yData,
        line = Line(color='rgba(255,0,0,1.0)'),
        mode = 'markers',
        name = 'Data',
        showlegend = True,
    )

    traceMean = Scatter(
        x    = xMean,
        y    = yMean,
        line = dict(
            width = 3,
            color = 'rgba(0,100,80, 1.0)'
        ),
        mode = 'lines',
        name = 'Media',
        showlegend = True,
    )

    # Se invierte el orden del borde inferior
    xInf = xInf[::-1]
    yInf = yInf[::-1]

    traceLimits = Scatter(
        x          = xSup+[None]+xInf,
        y          = ySup+[None]+yInf,
        fill       = 'tozeroy',
        #fill       = 'tozerox',
        #fill       = 'tonexty',
        #fill       = 'tonextx',
        fillcolor  = 'rgba(0,100,80,0.2)',
        line = dict(
            width = 2,
            color = 'rgba(0, 50, 0, 0.3)'
            #color='transparent'
        ),
        showlegend = True,
        name       = 'Confidence',
    )    

    plotData = [traceData, traceMean, traceLimits]

    plot(plotData, filename='test1.html')

if __name__ == "__main__":
    main()