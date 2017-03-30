# -*- coding: utf-8 -*-  
#!/usr/bin/python
#!/usr/bin/env python

# PASO 1: conda install -c clg_boar vtk=7.0.0
# PASO 2: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27
# PASO 3: pip install mayavi
# PASO 4: conda install -c anaconda wxpython=3.0.0.0

from __future__ import print_function
import numpy as np
import mayavi.mlab as mlab
import pandas as pd
import sys
from parula import parula

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def eprintDeb(stringData, debug, **kwargs):
    if debug == 1:
        print(stringData, file=sys.stderr, **kwargs)

def createDict(diccionario, categUnique, categUniqueLen):
    colorRGB  = parula(categUniqueLen, 0)
    colorRGB  = 255.0*colorRGB # Para que sean valores entre 0 y 255
    transp    = 255.0*np.ones((categUniqueLen,1))
    colorRGBA = np.concatenate((colorRGB, transp), axis = 1)
    #eprint(colorRGBA)
    dicDF = pd.DataFrame({ 'categ' : categUnique, 'R' : colorRGBA[:,0], 'G' : colorRGBA[:,1], 'B' : colorRGBA[:,2], 'A' : colorRGBA[:,3]})
    dicDF = dicDF[['categ','R','G','B','A']] # Se ordenan las columnas
    #eprint(dicDF)
    dicDF.to_csv(diccionario, index = False)

def getColorPoints(dataDict, categ):
    nDataIn = len(categ)
    categDicc = dataDict["categ"].tolist()
    RDicc     = dataDict["R"].tolist()
    GDicc     = dataDict["G"].tolist()
    BDicc     = dataDict["B"].tolist()
    ADicc     = dataDict["A"].tolist()
    nDataDicc = len(categDicc)
    colorRGBAdataIn = np.zeros((nDataIn, 4)) # 4 cols = R G B A
    for i in range(0, nDataIn): # Por cada muestra de entrada
        for j in range(0, nDataDicc): # Por cada muestra del diccionario
            if(categ[i] == categDicc[j]):
                colorRGBAdataIn[i, 0] = RDicc[j]# R
                colorRGBAdataIn[i, 1] = GDicc[j]# G
                colorRGBAdataIn[i, 2] = BDicc[j]# B
                colorRGBAdataIn[i, 3] = ADicc[j]# A
                break
    return colorRGBAdataIn

def plot3Dmayavi(xpos, ypos, zpos, colorRGBAdataIn, ballSize):
    N = len(xpos) # Number of points
    scalars = np.arange(N) # Key point: set an integer for each point
    x = xpos
    y = ypos
    z = zpos
    colors = colorRGBAdataIn
    s = [ballSize] * N # scale

    pts = mlab.quiver3d(x, y, z, s, s, s, scalars=scalars, mode='sphere', scale_factor=1) # Create points
    pts.glyph.color_mode = 'color_by_scalar' # Color by scalar
    pts.module_manager.scalar_lut_manager.lut.table = colors
    mlab.axes(x_axis_visibility = True)
    mlab.axes(y_axis_visibility = True)
    mlab.axes(z_axis_visibility = True)
    mlab.show()

def  main():
    ##############################################
    ## PARAMETROS
    ##############################################
    debug       = 1
    fileName    = "BD_lit.csv"
    xCol        = "x"
    yCol        = "y"
    zCol        = "z"
    categCol    = "categorica"
    diccionario = "categRGB.csv"
    ballSize    = 2

    ##############################################
    eprintDeb(" Archivo: " + fileName, debug)
    eprintDeb("        Reading " + fileName + " with pandas ...", debug)
    try:
        dataIn    = pd.read_csv(fileName, engine = 'c', memory_map = True)
    except IOError:
        eprint("\nERROR: El archivo: " + fileName + " NO existe")
        quit()

    xpos  = dataIn[xCol].tolist()
    ypos  = dataIn[yCol].tolist()
    zpos  = dataIn[zCol].tolist()
    categ = dataIn[categCol].tolist()

    # Se revisa si el archivo diccionario categRGB.csv existe. Si existe lo lee, si no lo crea.
    eprintDeb("        Reading dictionary " + diccionario + " with pandas ...", debug)
    try:
        eprint("El archivo diccionario: " + diccionario + " SI existe")
        dataDict    = pd.read_csv(diccionario, engine = 'c', memory_map = True)
        eprint("El diccionario es: ")
        eprint(dataDict)   

    except IOError:
        eprint("\nERROR: El archivo diccionario: " + diccionario + " NO existe, por lo tanto se crea.")
        categUnique = sorted(list(set(categ)))
        categUniqueLen = len(categUnique)
        eprint("categUniqueLen = " + str(categUniqueLen))
        eprint("Lista de categUnique ordenados: ")
        eprint(categUnique)
        eprint("\n")
        createDict(diccionario, categUnique, categUniqueLen)
        dataDict    = pd.read_csv(diccionario, engine = 'c', memory_map = True)
        eprint("El diccionario es: ")
        eprint(dataDict)   

    # Se generan los colores para cada punto dado el diccionario
    colorRGBAdataIn = getColorPoints(dataDict, categ)
    # Se muestra en 3D los datos
    plot3Dmayavi(xpos, ypos, zpos,colorRGBAdataIn, ballSize)

if __name__ == "__main__":
    main()