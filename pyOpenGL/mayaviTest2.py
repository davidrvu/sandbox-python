from tvtk.api import tvtk
from mayavi import mlab
import numpy as np

nr_points = 10
x,y,z  = np.random.random((3,nr_points)) #some data
colors = np.random.randint(256,size=(nr_points,3)) #some RGB or RGBA colors
colors = [[255,0,0],\
		 [255,0,0],\
		 [255,0,0],\
		 [255,0,0],\
		 [255,0,0],\
		 [0,255,0],\
		 [0,255,0],\
		 [0,255,0],\
		 [0,0,255],\
		 [0,0,255]]
print x
print y
print z
print colors

ballSize = 0.2
s = [ballSize] * len(x) # scale
c = np.random.random((1, len(x)))

#pts = mlab.points3d(x,y,z,s, scale_factor=1)
pts = mlab.quiver3d(x, y, z, s, s, s, scalars=c, mode='sphere')
#pts = mlab.points3d(x,y,z)

#pts.glyph.glyph.clamping = True

sc  = tvtk.UnsignedCharArray()
sc.from_array(colors)


pts.mlab_source.dataset.point_data.scalars = sc
pts.mlab_source.dataset.modified()


pts.glyph.color_mode = 'color_by_scalar'

mlab.axes(x_axis_visibility = True)
mlab.axes(y_axis_visibility = True)
mlab.axes(z_axis_visibility = True)
mlab.show()