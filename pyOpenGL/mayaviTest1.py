# PASO 1: python -m pip install --upgrade pip
# PASO 2: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27
# 			(INSTALAR Microsoft Visual C++ Compiler for Python 2.7)
# PASO 3: Instalar VTK para WINDOWS, desde http://www.vtk.org/download/
# PASO 4: conda install -c clg_boar vtk=7.0.0
# PASO 5: pip install mayavi
# PASO 6: conda install -c anaconda wxpython=3.0.0.0

#import enthought.mayavi.mlab as mylab
import mayavi.mlab as mlab
import numpy as np
import pandas as pd

#######################################################
## Se lee archivo
#######################################################
#filename = "BD_lito.csv"
filename = "BD_lito_mini.csv"
try:
    dataIn    = pd.read_csv(filename, engine = 'c', memory_map = True)
except IOError:
    print "\nERROR: El archivo: " + filename + " NO existe"
    quit()

#x, y, z, value = np.random.random((4, 40))

xCol = "mid_x"
yCol = "mid_y"
zCol = "mid_z"

x = np.array(dataIn[xCol].tolist())
y = np.array(dataIn[yCol].tolist())
z = np.array(dataIn[zCol].tolist())

x = np.transpose(x)
y = np.transpose(y)
z = np.transpose(z)

numMuestras = x.size
value = np.random.random((1, numMuestras))

print x.size
print y.size
print z.size
print value.size

#x, y, z, value = np.random.random((4, numMuestras))
#x = 2*x
#print x
#print value
#x = -1.0*x

#x = np.array([0, 20, 30, 1, 10])
#y = np.array([0, 50, 70, 1, 10])
#z = np.array([0, 60, 80, 1, 10])
#value = np.array([0.5, 0.5, 0.5, 0.5, 10])




x = [1, 2, 3, 4, 5, 6]
y = [0, 0, 0, 0, 0, 0]
z = y
#s = [.5, .6, .7, .8, .9, 1]
#s = [1, 1, 1, 1, 1, 1]
ballSize = 0.6
s = [ballSize] * len(x)

#c = [0.5] * len(x)
c = np.random.random((1, len(x)))
print x
print y
print z
print s
print c

#mlab.points3d(x, y, z, s, scale_factor=1)

#pts = mlab.quiver3d(x, y, z, s, s, s, scalars=c, mode='sphere')

pts = mlab.quiver3d(x, y, z, s, s, s, scalars=c, mode='sphere')
pts.glyph.color_mode = 'color_by_scalar'
# Finally, center the glyphs on the data point
pts.glyph.glyph_source.glyph_source.center = [0, 0, 0]

mlab.axes(x_axis_visibility = True)
mlab.axes(y_axis_visibility = True)
mlab.axes(z_axis_visibility = True)
mlab.show()