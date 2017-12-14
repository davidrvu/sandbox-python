# DAVIDRVU - 2017

from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Bar
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import os
import sys

def histogram_train_test_results(train_set_counts, test_correct, test_incorrect, histogram_fig_name, dictionary_labels, unique_labels, orientation):
    print("\n-> START histogram_train_test_results")

    train_set_counts_sorted = train_set_counts.sort_index()
    train_set_freq          = train_set_counts_sorted.values.tolist()
    test_correct            = list(test_correct)
    test_incorrect          = list(test_incorrect)

    #print(train_set_freq)
    #print(test_correct)
    #print(test_incorrect)

    # TODOTODO: CUSTOMIZAR COLORES DE LAS BARRAS
    # TODOTODO: TITLE
    # TODOTODO: Revisar valores de numeros de plotly con valores de csv

    #######################################
    # Bar Chart with Relative Barmode
    #######################################
    axis_titlefont_family = 'Courier New, monospace'
    axis_titlefont_size   = 20
    axis_titlefont_color  = '#7f7f7f'
    #title_plot            = title_in +  " | totalFreq = " + str(suma_total_freq) + " | Classes = " + str(names_array_len)
    title_plot            = "ASDASD"

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
            'barmode': 'relative'
        }

        trace1 = {
            'x': train_set_freq,
            'y': unique_labels,
            'name': "Train Set",
            'type': 'bar',
            'orientation': orientation
        }
        trace2 = {
            'x': test_correct,
            'y': unique_labels,
            'name': "Test correctly classified",
            'type': 'bar',
            'orientation': orientation
        }
        trace3 = {
            'x': test_incorrect,
            'y': unique_labels,
            'name': "Test incorrectly classified",
            'type': 'bar',
            'orientation': orientation
        }


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
            'barmode': 'relative'
        }

        trace1 = {
            'x': unique_labels,
            'y': train_set_freq,
            'name': "Train Set",
            'type': 'bar',
            'orientation': orientation
        }
        trace2 = {
            'x': unique_labels,
            'y': test_correct,
            'name': "Test correctly classified",
            'type': 'bar',
            'orientation': orientation
        }
        trace3 = {
            'x': unique_labels,
            'y': test_incorrect,
            'name': "Test incorrectly classified",
            'type': 'bar',
            'orientation': orientation
        }        
    else:
        print("\nERROR: orientation = " + orientation + " NO VALIDO.")
        sys.exit()

    data = [trace1, trace2, trace3]
    fig = dict(data = data, layout = layout)
    print("PLOTLY_HISTOGRAM_TRAIN_TEST histogram_fig_name = " + histogram_fig_name)

    directory = os.path.dirname(histogram_fig_name)
    if not os.path.exists(directory): # Si el directorio no existe, se crea
        print("Se crea el directorio: " + directory)
        os.makedirs(directory)

    plot(fig, filename=histogram_fig_name)
 
    print("----> END histogram_train_test_results\n")