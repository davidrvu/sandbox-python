# PASO 1: conda install -c clg_boar vtk=7.0.0
# PASO 2: pip install mayavi
# PASO 3: conda install -c anaconda wxpython=3.0.0.0

# Imports
import numpy as np
import mayavi.mlab as mlab

data = (100, 100, 100)
data = np.zeros(data)
data[0:50, 50:70, 0:50] = 1
data[0:50, 0:20, 0:50] = 1

xx, yy, zz = np.where(data == 1)

mlab.points3d(xx, yy, zz,
            mode="cube",
         	color=(0, 1, 0),
         	scale_factor=1)


mlab.axes(x_axis_visibility = True)
mlab.axes(y_axis_visibility = True)
mlab.axes(z_axis_visibility = True)
mlab.show()