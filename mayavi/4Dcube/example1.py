from mayavi import mlab
import numpy as np

x, y, z = np.ogrid[-2:2:20j, -2:2:20j, -2:2:20j]
s = np.sin(x*y*z + x + y*z)/(x*y*z + x + y*z)

mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                            plane_orientation='x_axes',
                            slice_index=20,
                        )
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                            plane_orientation='y_axes',
                            slice_index=20,
                        )
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                            plane_orientation='z_axes',
                            slice_index=20,
                        )
mlab.outline()
mlab.show()