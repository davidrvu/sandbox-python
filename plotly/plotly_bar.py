from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Bar
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import os
import sys

def plotly_bar(counts_array, names_array, filename, orientation, title_in):
    print("\n----> START plotly_bar")
    suma_total_freq  = sum(counts_array)
    counts_array_len = len(counts_array)
    names_array_len  = len(names_array)
    if(counts_array_len == names_array_len):
        print("counts_array_len == names_array_len")
    else:
        print("ERROR: counts_array_len != names_array_len")
        print("         counts_array_len = " + str(counts_array_len))
        print("         names_array_len  = " + str(names_array_len))
        sys.exit()
    ##################################################################
    
    ##################################################################
    ## PARAMETERS LAYOUT 
    ##################################################################
    axis_titlefont_family = 'Courier New, monospace'
    axis_titlefont_size   = 20
    axis_titlefont_color  = '#7f7f7f'
    title_plot            = title_in +  " | totalFreq = " + str(suma_total_freq) + " | Classes = " + str(names_array_len)

    if(orientation == "h"):
        layout = {
            'title': title_plot, 
            'xaxis': {
                'title': 'Frequency',
                'titlefont' : {
                    'family': axis_titlefont_family,
                    'size': axis_titlefont_size,
                    'color': axis_titlefont_color
                },       
                #'range': [0, 7]
            },
            'yaxis': {
                'title': 'Classes',
                'titlefont' : {
                    'family': axis_titlefont_family,
                    'size': axis_titlefont_size,
                    'color': axis_titlefont_color
                #'range': [0, 2.5]
                },
                'autorange': 'reversed'
            },
            'showlegend': False
        }
        trace1 = Bar(y=names_array, x=counts_array, orientation = orientation)
    elif (orientation == "v"):
        layout = {
            'title': title_plot, 
            'xaxis': {
                'title': 'Classes',
                'titlefont' : {
                    'family': axis_titlefont_family,
                    'size': axis_titlefont_size,
                    'color': axis_titlefont_color
                },       
                #'range': [0, 7]
                ##"rangeslider": { # SOLO PARA XAXIS ## DESCOMENTAR EN CASO DE QUERER EL RANGESLIDER
                ##  "autorange": True, 
                ##},
            },
            'yaxis': {
                'title': 'Frequency',
                'titlefont' : {
                    'family': axis_titlefont_family,
                    'size': axis_titlefont_size,
                    'color': axis_titlefont_color
                #'range': [0, 2.5]
                },
            },
            'showlegend': False
        }
        trace1 = Bar(x=names_array, y=counts_array, orientation = orientation)
    else:
        print("\nERROR: orientation = " + orientation + " NO VALIDO.")
        sys.exit()

    data = [trace1]
    fig = dict(data = data, layout = layout)
    print("PLOTLY_BAR filename = " + filename)

    directory = os.path.dirname(filename)
    if not os.path.exists(directory): # Si el directorio no existe, se crea
        print("Se crea el directorio: " + directory)
        os.makedirs(directory)

    plot(fig, filename=filename)
 
    print("----> END plotly_bar\n")