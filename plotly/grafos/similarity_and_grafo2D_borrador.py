# DAVIDRVU - 2018

from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Scatter3d, Margin
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from sklearn.metrics import pairwise_distances
import igraph as ig
import json
import matplotlib.pyplot as plt
import networkx as nx
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


def fromAffinityToGraph2D(debug, item_dissimilarity_jaccard, itemUnique, file_out):
    printDeb(debug, "\n----> START " + str(sys._getframe().f_code.co_name) )


    print("item_dissimilarity_jaccard = ")
    print(item_dissimilarity_jaccard)

    #item_similarity_jaccard = 1 - item_dissimilarity_jaccard

#######################################################################################################

#
#    #A = np.array([(0, 0.3, 0.4, 0.7),
#    #               (0.3, 0, 0.9, 0.2),
#    #               (0.4, 0.9, 0, 0.1),
#    #               (0.7, 0.2, 0.1, 0)
#    #               ])*10
#
#    A = np.array(item_similarity_jaccard)*10
#    #A = np.array(item_dissimilarity_jaccard)*100
#
#    #print("A = ")
#    #print(A)
#
#    
#
#
#    G = nx.from_numpy_matrix(A)
#
#
#
#######
#    pos = nx.random_layout(G) 
#
#    plt.figure(figsize=(7, 7))
#    for k, p in pos.iteritems():
#        plt.scatter(p[0], p[1], marker='o', c=colors[k], s=50, edgecolor='None')
#    lgd = plt.legend(markers, labels, numpoints=1, bbox_to_anchor=(1.17, 0.5))
#    plt.tight_layout()
#    plt.axis('equal')
#    pt.show()
#
#    sys.exit()
#
#######
#    #G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    
#
#    #G = nx.drawing.nx_agraph.to_agraph(G)
#
#    #G.node_attr.update(color="red", style="filled")
#    #G.edge_attr.update(color="blue", width="2.0")
#
#    #G.draw('out.png', format='png', prog='neato')
#
#    #sys.exit()
#
#    pos = nx.get_node_attributes(G,'pos')
#
#    dmin=1
#    ncenter=0
#    for n in pos:
#        x,y=pos[n]
#        d=(x-0.5)**2+(y-0.5)**2
#        if d<dmin:
#            ncenter=n
#            dmin=d
#
#    p=nx.single_source_shortest_path_length(G,ncenter)
#
#    ##########################################
#    # CREATE EDGES
#    ##########################################
#    edge_trace = Scatter(
#        x=[],
#        y=[],
#        line=dict(width=0.5,color='#888'),
#        hoverinfo='none',
#        mode='lines')
#
#    for edge in G.edges():
#        x0, y0 = G.node[edge[0]]['pos']
#        x1, y1 = G.node[edge[1]]['pos']
#        edge_trace['x'] += [x0, x1, None]
#        edge_trace['y'] += [y0, y1, None]
#
#    node_trace = Scatter(
#        x=[],
#        y=[],
#        text=[],
#        mode='markers',
#        hoverinfo='text',
#        marker=dict(
#            showscale=True,
#            # colorscale options
#            # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
#            # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
#            colorscale='YIGnBu',
#            reversescale=True,
#            color=[],
#            size=10,
#            colorbar=dict(
#                thickness=15,
#                title='Node Connections',
#                xanchor='left',
#                titleside='right'
#            ),
#            line=dict(width=2)))
#
#    for node in G.nodes():
#        x, y = G.node[node]['pos']
#        node_trace['x'].append(x)
#        node_trace['y'].append(y)
#
#    ##########################################
#    # COLOR NODE POINTS (by the number of connections)
#    ##########################################
#
#    #for node, adjacencies in enumerate(G.adj.items()):
#    for adjacencies in G.adjacency():
#        adjacencies = adjacencies[1]
#        node_trace['marker']['color'].append(len(adjacencies))
#        node_info = '# of connections: '+str(len(adjacencies))
#        node_trace['text'].append(node_info)
#
#    ##########################################
#    # CREATE NETWORK GRAPH
#    ##########################################
#
#    fig = Figure(data=[edge_trace, node_trace],
#                 layout=Layout(
#                    title='<br>Network graph made with Python',
#                    titlefont=dict(size=16),
#                    showlegend=False,
#                    hovermode='closest',
#                    margin=dict(b=20,l=5,r=5,t=40),
#                    annotations=[ dict(
#                        text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
#                        showarrow=False,
#                        xref="paper", yref="paper",
#                        x=0.005, y=-0.002 ) ],
#                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))
#
#    plot(fig, filename=file_out+"_grafo2D.html")
#
#    sys.exit()


#######################################################################################################


    ## Create graph, A.astype(bool).tolist() or (A / A).tolist() can also be used.
    #g = ig.Graph.Adjacency((item_dissimilarity_jaccard > 0).tolist())

    ## Add edge weights and node labels.
    #g.es['weight'] = item_dissimilarity_jaccard[item_dissimilarity_jaccard.nonzero()]
    #g.vs['label']  = itemUnique  # or a.index/a.columns

    N = len(itemUnique)

    #item_dissimilarity_jaccard = 1- item_dissimilarity_jaccard
    #print("item_dissimilarity_jaccard = ")
    #print(item_dissimilarity_jaccard)

    # get the row, col indices of the non-zero elements in your adjacency matrix
    threshold = 0.04 #0.1 #0.3 #0.5 # 0.0
    conn_indices = np.where(item_dissimilarity_jaccard > threshold)
    #conn_indices = np.where(A)

    # get the weights corresponding to these indices
    weights = item_dissimilarity_jaccard[conn_indices]
    #weights = A[conn_indices]

    # a sequence of (i, j) tuples, each corresponding to an edge from i -> j
    Edges = list(zip(*conn_indices))

    # initialize the graph from the edge sequence
    #G = ig.Graph(edges=Edges, directed=True)
    #G = ig.Graph.Adjacency(item_dissimilarity_jaccard)
    #G = ig.Graph.Adjacency((item_dissimilarity_jaccard > 0).tolist())
    G = ig.Graph.Adjacency((item_dissimilarity_jaccard > threshold).tolist())
    #G = ig.Graph.Adjacency((A > 0).tolist())
    


    # assign node names and weights to be attributes of the vertices and Edges
    # respectively
    G.vs['label']  = itemUnique   
    G.es['weight'] = weights

    # I will also assign the weights to the 'width' attribute of the Edges. this
    # means that igraph.plot will set the line thicknesses according to the edge
    # weights
    G.es['width'] = weights

    #print("G = ")
    #print(G)
    #print("Edges = ")
    #print(Edges)
    #print("weights = ")
    #print(weights)

    labels = itemUnique

    ##########################################
    # GET THE NODE POSITIONS
    ########################################## 

    # TODOTODO: REVISAR: https://stackoverflow.com/questions/38162607/revealing-clusters-of-interaction-in-igraph (PROBAR CON 2D)!!!!


    #layt=G.layout('kk', dim=3) # layt is a list of three elements lists (the coordinates of nodes)
    #layt=G.layout.fruchterman.reingold(weights=weights)
    #layt=G.layout('fr3d', weights=weights, dim=3)
    #layt=G.layout_drl(weights=weights, dim=3)

    #layt=G.layout('kk', dim=2) 
    #layt=G.layout_fruchterman_reingold(weights=20.0*weights, dim=2)
    #layt=G.layout_fruchterman_reingold(weights=[i * 20.0 for i in weights], dim=2)
    layt=G.layout_fruchterman_reingold(weights=weights, dim=2)



    ##########################################
    # SET THE DATA FOR THE PLOTLY PLOT
    ##########################################

    Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
    Yn=[layt[k][1] for k in range(N)]# y-coordinates
    #Zn=[layt[k][2] for k in range(N)]# z-coordinates
    Xe=[]
    Ye=[]
    Ze=[]
    Ce=[]
    We=[]
    for e in Edges:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]
        #Ze+=[layt[e[0]][2],layt[e[1]][2], None]
        #Ce+=['rgb(125,125,125)']
        Ce+=['rgb(200,0,0)']
        We+=[1.0] # weights

    EdgesLen = len(Edges)

    trace1=Scatter(x=Xe,
                   y=Ye,
                   #z=Ze,
                   mode='lines',
                   line=dict(color='rgb(125,125,125)', width=1),
                   hoverinfo='none'
                   )

    #trace1All = []
    #for i in range(0, EdgesLen):
    #    trace1All.append(Scatter3d(x=Xe[i],
    #               y=Ye[i],
    #               z=Ze[i],
    #               mode='lines',
    #               line=dict(color=Ce[i], width=We[i]),
    #               hoverinfo='none'
    #               ))


    trace1All = []
    for i in range(0, EdgesLen):
        trace1All.append(Scatter(
                   x=[layt[Edges[i][0]][0],layt[Edges[i][1]][0], None],
                   y=[layt[Edges[i][0]][1],layt[Edges[i][1]][1], None],
                   #z=[layt[Edges[i][0]][2],layt[Edges[i][1]][2], None],
                   mode='lines',
                   line=dict(color='rgb(125,125,125)', width=10.0*weights[i]),
                   hoverinfo='none'
                   ))


    trace2=Scatter(x=Xn,
                   y=Yn,
                   #z=Zn,
                   mode='markers',
                   name='actors',
                   marker=dict(symbol='dot',
                                 size=6,
                                 #color=group,
                                 colorscale='Viridis',
                                 line=dict(color='rgb(50,50,50)', width=0.5)
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
             title="Similarity 2D Graph",
             width=1000,
             height=1000,
             showlegend=False,
             scene=dict(
                 xaxis=dict(axis),
                 yaxis=dict(axis),
                 zaxis=dict(axis),
            ),
         margin=dict(
            t=100
        ),
        hovermode='closest',
        annotations=[
               dict(
               showarrow=False,
                text="DAVIDRVU - 2018",
                xref='paper',
                yref='paper',
                x=0,
                y=0.1,
                xanchor='left',
                yanchor='bottom',
                font=dict(
                size=14
                )
                )
            ],    )

    data=[trace1, trace2]
    #data = trace1All + [trace2]

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

    fromAffinityToGraph2D(debug, item_dissimilarity_jaccard, itemUnique, file_out)

    print("DONE!")

if __name__ == "__main__":
    main()