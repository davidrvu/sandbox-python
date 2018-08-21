# DAVIDRVU - 2018

from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Scatter3d, Margin
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from sklearn.metrics import pairwise_distances
import igraph as ig
import json
import numpy as np
import os
import plotly.figure_factory as ff
import string
import sys
import urllib.request

sys.path.insert(0, '../../data_science_utils')
from pandas_read_csv import pandas_read_csv
from printDeb import printDeb

# OJO: INSTALAR igraph para Windows:
# DESCARGAR: https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-igraph
# INSTALAR : python -m pip install C:\Users\drvalenzuela\Downloads\python_igraph-0.7.1.post6-cp36-cp36m-win_amd64.whl

def fromAffinityToDendrogram_plotly(debug, affinity_mat, itemUnique, file_out):
    printDeb(debug, "\n----> START " + str(sys._getframe().f_code.co_name) )

    fig = ff.create_dendrogram(affinity_mat, orientation='left', labels=itemUnique)

    fig['layout'].update({'width':800, 'height':800})
    fig['layout'].update({'margin':Margin({'l':200})})
    plot(fig, filename=file_out+"_dendrograma.html")

    printDeb(debug, "----> END " + str(sys._getframe().f_code.co_name) + "\n")


def fromAffinityToGraph2D(debug, item_dissimilarity_jaccard, itemUnique, th_dist, file_out):
    printDeb(debug, "\n----> START " + str(sys._getframe().f_code.co_name) )

    #print("item_dissimilarity_jaccard = ")
    #print(item_dissimilarity_jaccard)

    conn_indices = np.where(item_dissimilarity_jaccard > th_dist)

    # get the weights corresponding to these indices
    weights = item_dissimilarity_jaccard[conn_indices]

    # a sequence of (i, j) tuples, each corresponding to an edge from i -> j
    Edges = list(zip(*conn_indices))

    # initialize the graph from the edge sequence
    #G = ig.Graph(edges=Edges, directed=True)
    G = ig.Graph.Adjacency((item_dissimilarity_jaccard > th_dist).tolist())

    ##########################################
    # GET THE NODE POSITIONS
    ########################################## 
    #layt=G.layout('kk', dim=3) # layt is a list of three elements lists (the coordinates of nodes)
    #layt=G.layout.fruchterman.reingold(weights=weights)
    #layt=G.layout('fr3d', weights=weights, dim=3)
    #layt=G.layout_drl(weights=weights, dim=3)
    #layt=G.layout('kk', dim=2) 
    #layt=G.layout_fruchterman_reingold(weights=20.0*weights, dim=2)
    #layt=G.layout_fruchterman_reingold(weights=[i * 20.0 for i in weights], dim=2)
    layt = G.layout_fruchterman_reingold(weights=weights, dim=2)

    ##########################################
    # SET THE DATA FOR THE PLOTLY PLOT
    ##########################################
    totalNodes = len(itemUnique)
    print("totalNodes = " + str(totalNodes))
    Xn=[layt[k][0] for k in range(totalNodes)]# x-coordinates of nodes
    Yn=[layt[k][1] for k in range(totalNodes)]# y-coordinates
    ColorNode = [k for k in range(totalNodes)]
    Xe=[]
    Ye=[]
    for e in Edges:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]


    ##########################################
    # SET LABEL NODES
    ##########################################   
    labels    = [None] * totalNodes
    for i in range(0, totalNodes):
        labels[i] = "SKU          = " + str(itemUnique[i]) + "\n" #+ \
                    #"# conexiones = " + str(len(current_adj)) + "\n"

    #labels = itemUnique

    # LINES
    trace1=Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(150,150,150)', 
                             width=0.5
                            ),
                   hoverinfo='none'
                   )

    # NODES
    trace2=Scatter(x=Xn,
                   y=Yn,
                   mode='markers',
                   name='actors',
                   marker=dict(
                               showscale=True,
                               colorscale='Viridis',
                               reversescale=True,
                               symbol='dot',
                               size=10,
                               color=ColorNode,
                               colorbar=dict(
                                   thickness=15,
                                   title='CLUSTERS',
                                   xanchor='left',
                                   titleside='right'
                               ),                               
                               line=dict(color='rgb(150,150,150)',
                                         width=0.5
                                        )
                            ),
                   text=labels,
                   hoverinfo='text'
                   )

    axis=dict(showbackground=False,
              showline=False,
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              title=''
              )

    layout = Layout(
                    title="Similarity 2D Graph | totalNodes = " + str(totalNodes) + " | th_dist = " + str(th_dist),
                    width=1000,
                    height=1000,
                    showlegend=False,
                    xaxis = dict(axis),
                    yaxis = dict(axis),
                    scene=dict(
                        xaxis=dict(axis),
                        yaxis=dict(axis),
                        zaxis=dict(axis),
                    ),
                    margin=dict(
                        t=100
                    ),
                    hovermode='closest',
                    #annotations=[
                    #            dict(
                    #                showarrow=False,
                    #                text="th_dist = " + str(th_dist),
                    #                xref='paper',
                    #                yref='paper',
                    #                x=0,
                    #                y=0.05,
                    #                xanchor='left',
                    #                yanchor='bottom',
                    #                font=dict(
                    #                    size=14
                    #                )
                    #            )
                    #],    
            )

    data=[trace1, trace2]

    fig=Figure(data=data, layout=layout)

    print("Plot 2D...")
    plot(fig, filename=file_out+"_grafo2D.html")

    printDeb(debug, "----> END " + str(sys._getframe().f_code.co_name) + "\n")



def main():
    print("==============================================")
    print(" ---    SIMILARITY MATRIX AND GRAPH 2D    --- ")
    print("==============================================")

    ####################################################################
    # PARAMETROS
    ####################################################################

    debug     = 1
    #file_in   = "data_naveg.csv"
    #file_in   = "data_naveg2.csv"
    file_in   = "C:/databases/visitasWeb_J1101_from18-05-20.csv"

    #file_out  = "c:/graficos/similarity2D"
    file_out  = "c:/graficos/similarityWEB2D" 

    #userHeader = "ID_NAV_FINAL"
    userHeader = "ID_CLIENTE_NAV"
    itemHeader = "ID_SKU"

    th_dist    = 0.03 #0.04 #0.1 #0.3 #0.5 # 0.0

    ####################################################################


    df_in = pandas_read_csv(debug, file_in)

    #print("df_in = ")
    #print(df_in)

    userSerie  = df_in[userHeader]
    itemsSerie = df_in[itemHeader]

    userUnique = sorted(userSerie.unique())
    itemUnique = sorted(itemsSerie.unique())

    n_users = len(userUnique)
    n_items = len(itemUnique)
    printDeb(debug, "Number of users = " + str(n_users))
    printDeb(debug, "Number of items = " + str(n_items))

    ###################################################################
    printDeb(debug, "PREPROCESO -> ELIMINAR PARES USUARIO-ITEM REPETIDOS!")
    df_in_preproc = df_in.drop_duplicates()
    df_in_preproc = df_in_preproc.reset_index(drop=True)

    ###################################################################
    printDeb(debug, "PREPROCESO -> ELIMINAR USUARIOS CON SÓLO 1 VISITA!")
    user_counts      = df_in_preproc[userHeader].value_counts()
    user_counts_once = user_counts[user_counts == 1].index.values.tolist()

    #print("user_counts_once = ")
    #print(user_counts_once)

    df_in_preproc = df_in_preproc[~df_in_preproc[userHeader].isin(user_counts_once)]
    df_in_preproc = df_in_preproc.reset_index(drop=True)

    ###################################################################
    printDeb(debug, "PREPROCESO -> ELIMINAR ITEMS CON SÓLO 1 VISITA!")
    item_counts      = df_in_preproc[itemHeader].value_counts()
    item_counts_once = item_counts[item_counts == 1].index.values.tolist()
    df_in_preproc    = df_in_preproc[~df_in_preproc[itemHeader].isin(item_counts_once)]
    df_in_preproc    = df_in_preproc.reset_index(drop=True)

    ###################################################################

    userSerie  = df_in_preproc[userHeader]
    itemsSerie = df_in_preproc[itemHeader]

    total_rows = df_in_preproc.shape[0]

    userUnique = sorted(userSerie.unique())
    itemUnique = sorted(itemsSerie.unique())

    itemUniqueDict = {k: v for v, k in enumerate(itemUnique)}
    userUniqueDict = {k: v for v, k in enumerate(userUnique)}

    n_users = len(userUnique)
    n_items = len(itemUnique)
    printDeb(debug, "PREPROC Number of users = " + str(n_users))
    printDeb(debug, "PREPROC Number of items = " + str(n_items))
    printDeb(debug, "total_rows              = " + str(total_rows))

    ################################################&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    print("df_in_preproc = ")
    print(df_in_preproc)

    printDeb(debug, "ITEM-USER MATRIX ...") 
    item_user_matrix = np.zeros((n_items, n_users))
    for i in range(0,total_rows):
        print("i = " + str(i) + " de " + str(total_rows-1) + "    ", end="\r", flush=True)
        current_item = itemsSerie[i]
        current_user = userSerie[i]
        #user_index   = userUnique.index(current_user)
        #item_index   = itemUnique.index(current_item)
        #user_item_matrix[user_index, item_index] = 1
        item_user_matrix[itemUniqueDict.get(current_item), userUniqueDict.get(current_user)] = 1

    print("item_user_matrix = ")
    print(item_user_matrix)

    printDeb(debug, "item_visit_freq ...      ")
    item_visit_freq = list(np.sum(item_user_matrix, axis=1))

    #item_dissimilarity_cosine = 1 - pairwise_distances(item_user_matrix, metric='cosine')
    #print("item_dissimilarity_cosine = ")
    #print(item_dissimilarity_cosine)

    printDeb(debug, "From item_user_matrix to pairwise_distances -> metric: jaccard ...      ")
    item_dissimilarity_jaccard = 1 - pairwise_distances(item_user_matrix, metric='jaccard')
    print("item_dissimilarity_jaccard = ")
    print(item_dissimilarity_jaccard)

    fromAffinityToDendrogram_plotly(debug, item_dissimilarity_jaccard, itemUnique, file_out)

    fromAffinityToGraph2D(debug, item_dissimilarity_jaccard, itemUnique, th_dist, file_out)

    print("DONE!")

if __name__ == "__main__":
    main()