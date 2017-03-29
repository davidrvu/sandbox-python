# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

import numpy as np
import pandas as pd
import sys
from plot4Dbox import plot4Dbox
from getBoxInfo import getBoxInfo

def secuentialData(xSteps, ySteps, zSteps):
    data = np.array([])
    cont = 1
    for z in range(0,zSteps):
        ydata = np.array([]) 
        for y in range(0,ySteps):
            xdata = np.array([]) 
            for x in range(0,xSteps):
                xdata = np.append(xdata, [cont])
                cont = cont + 1
            if y == 0:
                ydata = xdata
            else:
                ydata = np.vstack([ydata, xdata])
        if z == 0:
            data = ydata
        else:
            data = np.dstack((data, ydata))
    return data

def main():
    # np.ogrid returns an open multi-dimensional “meshgrid”.
    xFrom  = -2
    xTo    = 2
    xSteps = 5j # 20j

    yFrom  = -2
    yTo    = 2
    ySteps = 5j # 20j

    zFrom  = -2
    zTo    = 2
    zSteps = 5j # 10j

    x, y, z = np.ogrid[xFrom:xTo:xSteps, yFrom:yTo:ySteps, zFrom:zTo:zSteps]
    #s = np.sin(x*y*z + x + y*z)/(x*y*z + x + y*z)
    #ss = x*y*z

    s = secuentialData(int(xSteps.imag), int(ySteps.imag), int(zSteps.imag))
    #print s
    #print "ss = "
    #print ss
    #print "s = "
    #print s
    #sys.exit()
    #print s
    #print " "
    #print x.size
    #print " "
    #print z.size
    #print " "
    #print s.size

    # para que inicialize la vista desde el centro del conjunto de bloques
    xViewIni = round(xSteps.imag/2)
    yViewIni = round(ySteps.imag/2)
    zViewIni = round(zSteps.imag/2)
    plot4Dbox(s, xViewIni, yViewIni, zViewIni)

if __name__ == "__main__":
    main()