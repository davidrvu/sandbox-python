# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

import numpy as np
from scipy import stats

def getBoxInfo(dataIn, xName, yName, zName):
    xunique = sorted(list(dataIn[xName].unique()))
    yunique = sorted(list(dataIn[yName].unique()))
    zunique = sorted(list(dataIn[zName].unique()))

    nx = len(xunique)
    ny = len(yunique)
    nz = len(zunique)

    xmin = min(xunique)
    ymin = min(yunique)
    zmin = min(zunique)

    dx_all = list(np.diff(xunique))
    dy_all = list(np.diff(yunique))
    dz_all = list(np.diff(zunique))

    if not dx_all: # Caso lista vacia
        dx_all = [0]
    if not dy_all: # Caso lista vacia
        dy_all = [0]
    if not dz_all: # Caso lista vacia
        dz_all = [0]

    dx = stats.mode(dx_all)[0][0]
    dy = stats.mode(dy_all)[0][0]
    dz = stats.mode(dz_all)[0][0]

    return BoxInfo(nx, ny, nz, xmin, ymin, zmin, dx, dy, dz)