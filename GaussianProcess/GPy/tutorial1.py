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
    pathPlots = "outputs/"
    # Si la carpeta no existe, se crea
    if not os.path.exists(pathPlots):
        os.makedirs(pathPlots)

    #######################
    ## PARAMETROS
    #######################

    outputFileSinOpt = pathPlots + 'test1_sinOpt.html'
    outputFileConOpt = pathPlots + 'test1_conOpt.html'
    outputFileAll    = pathPlots + 'test1.html'
    mLegendAll       = []
    mColorAll        = []

    #######################
    ## Definiciones
    #######################
    GPy.plotting.change_plotting_library('plotly')

    numPuntos = 100

    X = np.random.uniform(-3.,3.,(numPuntos,1))
    Y = np.sin(X) + np.random.randn(numPuntos,1)*0.05 #Y include some noise.

    #The first step is to define the covariance kernel we want to use for the model.
    kernel = GPy.kern.RBF(input_dim=1, variance=1.0, lengthscale=1.)


    #The parameter input_dim stands for the dimension of the input space. 
    #The parameters variance and lengthscale are optional, and default to 1. 
    #Many other kernels are implemented, type GPy.kern.<tab> to see a list

    #The inputs required for building the model are the observations and the kernel:
    m = GPy.models.GPRegression(X,Y,kernel)
    
    mSinOptimizar = m
    mLegend = ['Data sin Opt','Media sin Opt','Confidence sin Opt']
    mLegendAll.append(mLegend)
    plotlyGPy([m], [mLegend], mColorAll, outputFileSinOpt)

    #Optimization
    m.optimize(messages=True)
    m.optimize_restarts(num_restarts = 10)

    mOptimo = m
    mLegend = ['Data Optimo','Media Optimo','Confidence Optimo']
    mLegendAll.append(mLegend)

    plotlyGPy([m], [mLegend], mColorAll, outputFileConOpt)

    #Graficos de todos los casos
    mGroup = [mSinOptimizar, mOptimo]
    plotlyGPy(mGroup, mLegendAll, mColorAll, outputFileAll)

if __name__ == "__main__":
    main()