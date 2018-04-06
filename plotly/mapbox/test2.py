# DAVIDRVU 2018

from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np

def main():
    mapbox_access_token = 'pk.eyJ1IjoiZGF2aWRydnUiLCJhIjoiY2pmYmsxbGY0MGhoYTJ3bWlobTZ5dzJiNSJ9.Mk0hRLld7K0BJrbvnv_7Ka'
    mg_values = [23700.0, 27500.0] # nT
    lat       = [-33.444612, -45.571179]
    lon       = [-70.656512, -72.068399]
    text_data = ["sensor_1","sensor_2"]

    for i in range(0, len(text_data)):
        text_data[i] = text_data[i] + ": " + str(mg_values[i]) + " [nT]"

    lat_mean = np.mean(lat)
    lon_mean = np.mean(lon)

    print("lat_mean = " + str(lat_mean))
    print("lon_mean = " + str(lon_mean))


    lat_str = ['{:.6f}'.format(x) for x in lat]
    lon_str = ['{:.6f}'.format(x) for x in lon]

    data = Data([
        Scattermapbox(
            lat = lat_str,
            lon = lon_str,
            mode = 'markers',
            marker=Marker(
                size =17,
                color = mg_values, #set color equal to a variable
                colorscale='Viridis',
                showscale=True,
                opacity=0.8
            ),
            text=text_data,
            #hoverinfo='text',

            ## TODOTODO: ??
            ##stream=dict(       
            ##    token="aaa",
            ##    maxpoints=200
            ##)
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

    fig = dict(data=data, layout=layout)
    plot(fig, filename='nT_map.html')

if __name__ == "__main__":
    main()