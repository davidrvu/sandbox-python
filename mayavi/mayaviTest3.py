# PASO 1: conda install -c clg_boar vtk=7.0.0
# PASO 2: pip install mayavi
# PASO 3: conda install -c anaconda wxpython=3.0.0.0

# Imports
import numpy as np
from mayavi.mlab import quiver3d, draw
import mayavi.mlab as mlab

# Primitives
N = 10 # Number of points
ones = np.ones(N)
scalars = np.arange(N) # Key point: set an integer for each point

# Define color table (including alpha), which must be uint8 and [0,255]
#colors = (np.random.random((N, 4))*255).astype(np.uint8)
#colors[:,-1] = 255 # No transparency
colors = np.zeros((N, 4))

print colors
# Define coordinates and points
##x, y, z = colors[:,0], colors[:,1], colors[:,2] # Assign x, y, z values to match color

#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## TODOTODO: 1) leer csv con data.
#			 2) Seleccionar x y z y categorica
#            3) Leer archivo categRGB.csv. Si no existe, se crea (diccionario con categ Unique)
#            4) Se lee el diccionario categRGB.csv: Categ R G B (de 0 a 255)
#			 5) Se generan los colores para cada punto dado el diccionario
#            6) Se muestran las posiciones de los puntos

x = 100.0*(np.random.random((1,N))-0.5)
y = 100.0*(np.random.random((1,N))-0.5)
z = 100.0*(np.random.random((1,N))-0.5)

x = x[0,:]
y = y[0,:]
z = z[0,:]


print x
print y
print z

colors[:,0] = [255, 255, 255, 255, 0, 0, 0, 0, 0, 0] # RED
colors[:,1] = [0, 0, 0, 0, 255, 255, 255, 255, 0, 0] # GREEN
colors[:,2] = [0, 0, 0, 0, 0, 0, 0, 0, 255, 255]     # BLUE
colors[:,3] = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255] # Transparency

print colors

ballSize = 10
s = [ballSize] * len(x) # scale
print s

pts = quiver3d(x, y, z, s, s, s, scalars=scalars, mode='sphere', scale_factor=1) # Create points
pts.glyph.color_mode = 'color_by_scalar' # Color by scalar

# Set look-up table and redraw
pts.module_manager.scalar_lut_manager.lut.table = colors
#draw()

mlab.axes(x_axis_visibility = True)
mlab.axes(y_axis_visibility = True)
mlab.axes(z_axis_visibility = True)
mlab.show()