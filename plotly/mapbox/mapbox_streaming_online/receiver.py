# DAVIDRVU 2018

# SOURCE: https://stackoverflow.com/questions/28161244/how-to-create-two-y-axes-streaming-plotly

from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis, Scattermapbox, Marker
import datetime
import numpy as np
import plotly.plotly as py # plotly library
import sys
import time

def main():
    print("RECEIVER AND PLOT")

    # Plot.ly credentials and stream tokens
    username            = 'davidrvu'
    api_key             = 'hOQ0feXyuUxZ0WtrhUgt'
    stream_token        = 'aghuvyozmm'
    mapbox_access_token = 'pk.eyJ1IjoiZGF2aWRydnUiLCJhIjoiY2pmYmsxbGY0MGhoYTJ3bWlobTZ5dzJiNSJ9.Mk0hRLld7K0BJrbvnv_7KA'

    print("py.sign_in ...")
    py.sign_in(username, api_key)
    print("py.sign_in DONE!")


    ####################################################################################################
    lat       = [-33.444612, -45.571179]
    lon       = [-70.656512, -72.068399]

    lat_mean = np.mean(lat)
    lon_mean = np.mean(lon)

    print("lat_mean = " + str(lat_mean))
    print("lon_mean = " + str(lon_mean))

    ####################################################################################################
    data = Data([
                Scattermapbox(
                    lat = [],
                    lon = [],
                    mode = "markers",
                    marker=Marker(
                        size = [],
                        color = [], #set color equal to a variable
                        colorscale='Viridis',
                        showscale=True,
                        opacity=0.8
                    ),
                    text=[],
                    #hoverinfo='text',
                    stream=Stream(
                         token=stream_token,
                         #maxpoints=200
                    ),
                    
                )
            ])

    layout = Layout(
        title="nT",
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=lat_mean,
                lon=lon_mean
            ),
            pitch=0,
            zoom=4,
            style='light'
        ),
    )

    fig = Figure(data=data, layout=layout)
    print(py.plot(fig, filename='Plotly mapbox streaming test'))

if __name__ == "__main__":
    main()