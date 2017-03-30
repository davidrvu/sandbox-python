# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/usr/bin/env python

from mayavi import mlab
import numpy as np

def plot4Dbox(data, xIni, yIni, zIni):
    print "xIni = " + str(xIni) + " | yIni = " + str(yIni) + " | zIni = " + str(zIni)
    # Se inicializa la ventana de Mayavi (Background)
    mlab.figure(size = (1024,768), bgcolor = (0.0,0.0,0.0))

    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                                plane_orientation='x_axes',
                                slice_index=xIni,
                                name='x',
                                #colormap='cool',
                                #colormap='Spectral',
                                colormap='jet',
                            )
    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                                plane_orientation='y_axes',
                                slice_index=yIni,
                                name='y',
                                #colormap='cool',
                                #colormap='Spectral',
                                colormap='jet',
                            )
    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data),
                                plane_orientation='z_axes',
                                slice_index=zIni,
                                name='z',
                                #colormap='cool',
                                #colormap='Spectral',
                                colormap='jet',
                            )
    mlab.outline()
    mlab.axes(x_axis_visibility = True)
    mlab.axes(y_axis_visibility = True)
    mlab.axes(z_axis_visibility = True)

    #mesh.module_manager.scalar_lut_manager.show_scalar_bar = True
    #mlab.colorbar(title='colorbar',orientation='vertical',nb_labels=2,nb_colors=10,label_fmt='%.1f')
    mlab.scalarbar(title='colorbar',orientation='vertical',nb_labels=2,nb_colors=10,label_fmt='%.1f')
   
    mlab.show()