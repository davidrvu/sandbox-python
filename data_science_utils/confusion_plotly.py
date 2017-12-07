# DAVIDRVU - 2017
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Bar
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import os
import plotly.figure_factory as ff
import plotly.plotly as pp

def confusion_plotly(conf_matrix, algo_performance, figure_name, dictionary_labels, unique_labels):
    print("\n-> START confusion_plotly")
    print("figure_name = " + figure_name)

    figure_name_html = figure_name + ".html"
    figure_name_png  = figure_name + ".png"

    print("figure_name_html = " +  figure_name_html)
    print("figure_name_png  = " +  figure_name_png)

    print("dictionary_labels = ")
    print(dictionary_labels)
    avg_precision_score = algo_performance.avg_precision_score
    avg_recall_score    = algo_performance.avg_recall_score   
    avg_f1_score        = algo_performance.avg_f1_score       
    acc_score           = algo_performance.acc_score      

    title_plot            = "Confusion Matrix" +  " |Precision=" + str(avg_precision_score) + " |Recall=" + str(avg_recall_score) + " |f1=" + str(avg_f1_score) + " |Accuracy=" + str(acc_score)

    if dictionary_labels is None:
        print("No hay diccionario!")
        x = unique_labels
        y = unique_labels        
    else: 
        print("Hay diccionario!")
        inv_dictionary_labels = {v: k for k, v in dictionary_labels.items()}
        unique_labels_len = len(unique_labels)
        x = []
        y = []
        for i in range(1, unique_labels_len+1):
            current_label = inv_dictionary_labels.get(i)
            x.append(current_label)
            y.append(current_label)

    fig = ff.create_annotated_heatmap(conf_matrix, x=x, y=y, colorscale='Reds')
    fig.layout.title           = title_plot
    fig.layout.xaxis.side      = 'bottom'
    fig.layout.xaxis.title     = "Predicted class"
    fig.layout.yaxis.title     = "True class"
    fig.layout.yaxis.autorange = "reversed"

    directory = os.path.dirname(figure_name_html)
    if not os.path.exists(directory): # Si el directorio no existe, se crea
        print("Se crea el directorio: " + directory)
        os.makedirs(directory)

    plot(fig, filename=figure_name_html, image='png')
