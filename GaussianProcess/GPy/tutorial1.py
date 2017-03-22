# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

# pip install gpy
# HELP GPy    > http://nbviewer.jupyter.org/github/SheffieldML/notebook/blob/master/GPy/basic_gp.ipynb
# HELP PLOTLY > https://plot.ly/python/line-charts/

import os
import GPy
import numpy as np
from plotlyGPy import plotlyGPy

def main():
    print "#################################################"
    print "## Gaussian process regression tutorial"
    print "##    -> 1-dimensional model"
    print "#################################################"
    titulo = "Gaussian process regression tutorial - 1D model"
    pathPlots = "outputs/"
    # Si la carpeta no existe, se crea
    if not os.path.exists(pathPlots):
        os.makedirs(pathPlots)

    ##############################################
    ## PARAMETROS
    ##############################################

    outputFileSinOpt = pathPlots + 'test1_sinOpt.html'
    outputFileConOpt = pathPlots + 'test1_conOpt.html'
    outputFileAll    = pathPlots + 'test1.html'
    mLegendAll       = []
    mColorAll        = [] # TODOTODO definir colores

    ##############################################
    ## Definiciones
    ##############################################
    GPy.plotting.change_plotting_library('plotly')

    numPuntos = 100

    X = np.random.uniform(-3.,3.,(numPuntos,1))
    Y = np.sin(X) + np.random.randn(numPuntos,1)*0.05 #Y include some noise.

    #The first step is to define the covariance kernel we want to use for the model.
    kernel = GPy.kern.RBF(input_dim=1, variance=1.0, lengthscale=1.0)
    #The parameter input_dim stands for the dimension of the input space. 
    #The parameters variance and lengthscale are optional, and default to 1. 
    #Many other kernels are implemented, type GPy.kern.<tab> to see a list

    ##############################################
    ## Se crea el modelo
    ##############################################
    #The inputs required for building the model are the observations and the kernel:
    mSinOptimizar   = GPy.models.GPRegression(X,Y,kernel)
    figSinOptimizar = mSinOptimizar.plot()
    
    mLegend = ['Data sin Opt','Media sin Opt','Confidence sin Opt']
    mLegendAll.append(mLegend)
    plotlyGPy([figSinOptimizar], [mLegend], mColorAll, outputFileSinOpt, titulo)
    #The shaded region corresponds to ~95% confidence intervals (ie +/- 2 standard deviation).

    ##############################################
    ## Se optimiza el modelo
    ##############################################
    mOptimo = mSinOptimizar

    # A common approach is to find the values of the parameters that maximize the likelihood of the data.
    mOptimo.optimize(messages=True)

    # If we want to perform some restarts to try to improve the result of the optimization, we can use the optimize_restarts function. 
    # This selects random (drawn from N(0,1)N(0,1)) initializations for the parameter values, optimizes each, 
    # and sets the model to the best solution found.
    mOptimo.optimize_restarts(num_restarts = 10)
    figOptimo = mOptimo.plot()

    mLegend = ['Data Optimo','Media Optimo','Confidence Optimo']
    mLegendAll.append(mLegend)

    plotlyGPy([figOptimo], [mLegend], mColorAll, outputFileConOpt, titulo)
    # The parameters values have been optimized against the log likelihood 
    # (aka the log marginal likelihood): the fit should be much better.

    ##############################################
    ## Se grafican ambos modelos juntos
    ##############################################
    figGroup = [figSinOptimizar, figOptimo]
    plotlyGPy(figGroup, mLegendAll, mColorAll, outputFileAll, titulo)

if __name__ == "__main__":
    main()