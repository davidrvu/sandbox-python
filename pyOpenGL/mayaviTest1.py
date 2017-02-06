# PASO 1: python -m pip install --upgrade pip
# PASO 2: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27
# 			(INSTALAR Microsoft Visual C++ Compiler for Python 2.7)
# PASO 3: Instalar VTK para WINDOWS, desde http://www.vtk.org/download/
# PASO 4: conda install -c clg_boar vtk=7.0.0
# PASO 5: pip install mayavi
# PASO 6: conda install -c anaconda wxpython=3.0.0.0

#import enthought.mayavi.mlab as mylab
import mayavi.mlab as mylab
import numpy as np
x, y, z, value = np.random.random((4, 40))
mylab.points3d(x, y, z, value)
mylab.show()