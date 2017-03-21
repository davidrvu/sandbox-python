# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *

def printDataFromGPYplot(i, figGroupLen, fig):
	print "######################################################"
	print "Iteracion: " + str(i) + " de " + str(figGroupLen-1)
	print fig
	print "######################################################"

def plotlyGPy(figGroup, legendAll, mColorAll, outputFile):
	figGroupLen = len(figGroup)

	plotDataAll = []

	for i in range(0, figGroupLen):
		fig       = figGroup[i]
		figLegend = legendAll[i]

		#printDataFromGPYplot(i, figGroupLen, fig)

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
			name = figLegend[0],
			showlegend = True,
		)

		# Create a trace
		traceMean = Scatter(
			x    = xMean,
			y    = yMean,
			line = dict(
				width = 3,
				color = 'rgba(0,100,80, 1.0)'
			),
			mode = 'lines',
			#name = 'Media',
			name = figLegend[1],
			showlegend = True,
		)

		# Se invierte el orden del borde inferior
		xInf = xInf[::-1]
		yInf = yInf[::-1]

		# Create a trace
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
			#name = 'Confidence',
			name = figLegend[2],
		)    
		plotData = [traceLimits, traceMean, traceData]
		plotDataAll = plotDataAll + plotData

	dataAll = Data(plotDataAll)
	figAll  = Figure(data=dataAll)#, layout=layout)
	plot(figAll, filename=outputFile)