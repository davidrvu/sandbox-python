# DAVIDRVU - 2018

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl, Scatter3d
import igraph as ig
import json
import urllib.request

# OJO: INSTALAR igraph para Windows:
# DESCARGAR: https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-igraph
# INSTALAR : python -m pip install C:\Users\drvalenzuela\Downloads\python_igraph-0.7.1.post6-cp36-cp36m-win_amd64.whl

def main():
    print("=========================")
    print(" --- PLOTLY GRAFO 3D --- ")
    print("=========================")

    ##########################################
    # READ GRAPH DATA FROM JSON FILE
    ##########################################
    data = []
    url = "https://raw.githubusercontent.com/plotly/datasets/master/miserables.json"
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    data = json.loads(r.decode('utf-8'))

    ##########################################
    # GET THE NUMBER OF NODES
    ##########################################

    N=len(data['nodes'])

    ##########################################
    # LIST OF THE EDGES AND THE GRAPH OBJECT FROM EDGES
    ##########################################

    L=len(data['links'])
    Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]

    G=ig.Graph(Edges, directed=False)

    ##########################################
    # EXTRACT THE NODE ATTRIBUTES
    ##########################################
    labels=[]
    group=[]
    for node in data['nodes']:
        labels.append(node['name'])
        group.append(node['group'])


    ##########################################
    # GET THE NODE POSITIONS
    ##########################################
    layt=G.layout('kk', dim=3) # layt is a list of three elements lists (the coordinates of nodes)
 
    ##########################################
    # SET THE DATA FOR THE PLOTLY PLOT
    ##########################################

    Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
    Yn=[layt[k][1] for k in range(N)]# y-coordinates
    Zn=[layt[k][2] for k in range(N)]# z-coordinates
    Xe=[]
    Ye=[]
    Ze=[]
    for e in Edges:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]
        Ze+=[layt[e[0]][2],layt[e[1]][2], None]



    trace1=Scatter3d(x=Xe,
                   y=Ye,
                   z=Ze,
                   mode='lines',
                   line=dict(color='rgb(125,125,125)', width=1),
                   hoverinfo='none'
                   )
    trace2=Scatter3d(x=Xn,
                   y=Yn,
                   z=Zn,
                   mode='markers',
                   name='actors',
                   marker=dict(symbol='dot',
                                 size=6,
                                 color=group,
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
             title="Network of coappearances of characters in Victor Hugo's novel<br> Les Miserables (3D visualization)",
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
                text="Data source: <a href='http://bost.ocks.org/mike/miserables/miserables.json'>[1] miserables.json</a>",
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
    fig=Figure(data=data, layout=layout)

    plot(fig, filename='c:/graficos/grafo3D.html')

    print("DONE!")


if __name__ == "__main__":
    main()