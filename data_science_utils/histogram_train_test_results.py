# DAVIDRVU - 2017

from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Bar
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import os
import sys

def histogram_train_test_results(algo_performance, train_set_counts, test_correct, test_incorrect, histogram_fig_name, dictionary_labels, unique_labels, accuracy_per_class, orientation):
    print("\n-> START histogram_train_test_results")

    train_set_counts_sorted = train_set_counts.sort_index()
    train_set_freq          = train_set_counts_sorted.values.tolist()
    test_correct            = list(test_correct)
    test_incorrect          = list(test_incorrect)

    unique_labels_len       = len(unique_labels)

    sum_train_set_freq      = sum(train_set_freq)
    sum_test_correct        = sum(test_correct)
    sum_test_incorrect      = sum(test_incorrect)

    suma_total_freq         = sum([sum_train_set_freq, sum_test_correct, sum_test_incorrect])

    y_ticks = []
    if dictionary_labels is None:
        print("No hay diccionario!")
        for i in range(0, unique_labels_len):
            current_label_acc = "Class " + str(unique_labels[i]) + " " + str(int(round(accuracy_per_class[i],2)*100.0)) + "%"
            y_ticks.append(current_label_acc)     
    else: 
        print("Hay diccionario!")
        inv_dictionary_labels = {v: k for k, v in dictionary_labels.items()}
        for i in range(1, unique_labels_len+1):
            current_label     = inv_dictionary_labels.get(i)
            current_label_acc = current_label + " " + str(int(round(accuracy_per_class[i-1],2)*100.0)) + "%"
            y_ticks.append(current_label_acc)

    #######################################
    # Bar Chart with Relative Barmode
    #######################################
    axis_titlefont_family = 'Courier New, monospace'
    axis_titlefont_size   = 20
    axis_titlefont_color  = '#7f7f7f'

    avg_precision_score = algo_performance.avg_precision_score
    avg_recall_score    = algo_performance.avg_recall_score   
    avg_f1_score        = algo_performance.avg_f1_score       
    acc_score           = algo_performance.acc_score      

    title_plot            = "Histogram | totalFreq = " + str(suma_total_freq) + " | Classes = " + str(unique_labels_len) + " |Precision=" + str(avg_precision_score) + " |Recall=" + str(avg_recall_score) + " |f1=" + str(avg_f1_score) + " |Accuracy=" + str(acc_score)

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
            'barmode': 'relative',
            'margin': {
                'l': 170
            }
        }

        trace1 = {
            'x': train_set_freq,
            'y': y_ticks,
            'name': "Train Set (" + str(sum_train_set_freq) + ")",
            'type': 'bar',
            'orientation': orientation,
            'marker': {
                'color': 'rgb(0,0,204)'
            }
        }
        trace2 = {
            'x': test_correct,
            'y': y_ticks,
            'name': "Test correctly classified (" + str(sum_test_correct) + ")",
            'type': 'bar',
            'orientation': orientation,
            'marker': {
                'color': 'rgb(0,204,0)'
            }
        }
        trace3 = {
            'x': test_incorrect,
            'y': y_ticks,
            'name': "Test incorrectly classified (" + str(sum_test_incorrect) + ")",
            'type': 'bar',
            'orientation': orientation,
            'marker': {
                'color': 'rgb(204,0,0)'
            }
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
            'x': y_ticks,
            'y': train_set_freq,
            'name': "Train Set (" + str(sum_train_set_freq) + ")",
            'type': 'bar',
            'orientation': orientation,
            'marker': {
                'color': 'rgb(0,0,204)'
            }
        }
        trace2 = {
            'x': y_ticks,
            'y': test_correct,
            'name': "Test correctly classified (" + str(sum_test_correct) + ")",
            'type': 'bar',
            'orientation': orientation,
            'marker': {
                'color': 'rgb(0,204,0)'
            }
        }
        trace3 = {
            'x': y_ticks,
            'y': test_incorrect,
            'name': "Test incorrectly classified (" + str(sum_test_incorrect) + ")",
            'type': 'bar',
            'orientation': orientation,
            'marker': {
                'color': 'rgb(204,0,0)'
            }
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

    if (unique_labels_len < 10):
        image_width_param  = 800
        image_height_param = 600
    else:
        image_width_param  = 1920
        image_height_param = 1080    

    plot(fig, filename=histogram_fig_name, image='png', image_width=image_width_param, image_height=image_height_param)
 
    print("----> END histogram_train_test_results\n")