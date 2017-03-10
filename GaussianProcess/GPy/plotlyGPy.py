# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Line

def plotlyGPy(mGroup, mLegendAll, mColorAll, outputFile):
    mGroupLen = len(mGroup)

    plotDataAll = []

    for i in range(0, mGroupLen):
        m       = mGroup[i]
        mLegend = mLegendAll[i]

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
            #name = 'Data',
            name = mLegend[0],
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
            #name = 'Media',
            name = mLegend[1],
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
            #name       = 'Confidence',
            name = mLegend[2],
        )    
        #plotData = [traceData, traceMean, traceLimits]
        plotData = [traceLimits,traceData, traceMean]
        plotDataAll = plotDataAll + plotData

    plot(plotDataAll, filename=outputFile)