# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

from mayavi import mlab
import numpy as np

def plot4Dbox(data, xIni, yIni, zIni):
    # Se inicializa la ventana de Mayavi (Background)
    mlab.figure(size = (1024,768), bgcolor = (0.0,0.0,0.0))

    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                                plane_orientation='x_axes',
                                slice_index=xIni,
                                #colormap='cool',
                            )
    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                                plane_orientation='y_axes',
                                slice_index=yIni,
                                #colormap='cool',
                            )
    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                                plane_orientation='z_axes',
                                slice_index=zIni,
                                #colormap='cool',
                            )
    mlab.outline()
    mlab.axes(x_axis_visibility = True)
    mlab.axes(y_axis_visibility = True)
    mlab.axes(z_axis_visibility = True)

    #mesh.module_manager.scalar_lut_manager.show_scalar_bar = True
    mlab.colorbar(orientation='vertical',nb_labels=2,label_fmt='%.1f')
    mlab.show()