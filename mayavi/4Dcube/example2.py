# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

import numpy as np
from plot4Dbox import plot4Dbox

def main():
    # np.ogrid returns an open multi-dimensional “meshgrid”.
    x, y, z = np.ogrid[-2:2:20j, -2:2:20j, -2:2:20j]
    s = np.sin(x*y*z + x + y*z)/(x*y*z + x + y*z)
    #s = x*y*z
    #print s

    xIni = 20
    yIni = 20
    zIni = 20
    plot4Dbox(s, xIni, yIni, zIni)

if __name__ == "__main__":
    main()