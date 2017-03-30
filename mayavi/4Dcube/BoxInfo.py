# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

from scipy import stats #stats de scipy se usa solamente aca (al 23/03/2017) y su importacion es lenta. No incluir en ImportUtil

class BoxInfo(object):
    def __init__(self, nx, ny, nz, xmin, ymin, zmin, dx, dy, dz, xmax, ymax, zmax):
        self.nx   = nx
        self.ny   = ny
        self.nz   = nz
        self.xmin = xmin
        self.ymin = ymin
        self.zmin = zmin
        self.dx   = dx
        self.dy   = dy
        self.dz   = dz
        self.xmax = xmax
        self.ymax = ymax
        self.zmax = zmax