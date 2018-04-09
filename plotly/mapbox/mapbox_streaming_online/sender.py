# DAVIDRVU 2018

# SOURCE: https://stackoverflow.com/questions/28161244/how-to-create-two-y-axes-streaming-plotly

from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis, Scattermapbox, Marker
import datetime
import numpy as np
import plotly.plotly as py # plotly library
import sys
import time


def main():
    print("SENDER DATA")

    stream_token = 'aghuvyozmm'

    stream_mag = py.Stream(stream_token)
    stream_mag.open()

    x_count = 0 
    freq1   = 10
    freq2   = 30
    Fs      = 100

    nT_min  = 20000 # nT
    nT_max  = 40000 # nT

    nT_amp  = (nT_max - nT_min)/2.0
    nT_mean = np.mean([nT_max, nT_min])

    print("nT_amp  = " + str(nT_amp))
    print("nT_mean = " + str(nT_mean))
 
    ##mg_values   = [23700.0, 27500.0] # nT (BORRAR)

    # TODOTODO: agregar punto max y min en antartica para que no se mueva la escala!!!!


    lat         = [-33.444612, -45.571179, -90.0, -90.0]
    lon         = [-70.656512, -72.068399,   0.0,   0.0]
    sensor_name = ["sensor_1", "sensor_2", "min_val", "max_val"]
    text_data   = [""] * len(sensor_name)

    lat_str = ['{:.6f}'.format(x) for x in lat]
    lon_str = ['{:.6f}'.format(x) for x in lon]

    print("Starting main loop ...")

    while(True):
        #print("x_count = " + str(x_count))
        
        nT1 = round((nT_amp * np.sin(2 * np.pi * freq1 * x_count / Fs) + 0         ) + nT_mean , 3)
        nT2 = round((nT_amp * np.sin(2 * np.pi * freq2 * x_count / Fs) + (np.pi/2.0) ) + nT_mean , 3)

        mg_values = [nT1, nT2, nT_min, nT_max] # nT

        time_now = datetime.datetime.now()

        print(str(time_now) + " | nT1 = " + str(nT1) + " | nT2 = " + str(nT2) + "    | x_count = " + str(x_count))

        for i in range(0, len(sensor_name)):
            text_data[i] = str(time_now) + " | " + sensor_name[i] + ": " + str(mg_values[i]) + " [nT]" 

        stream_mag.write(Scattermapbox(lat=lat_str, 
                                       lon=lon_str,
                                       mode = 'markers',
                                       marker=Marker(
                                           size =25,
                                           color = mg_values, #set color equal to a variable
                                           colorscale='Viridis',
                                           showscale=True,
                                           opacity=0.8
                                       ),
                                       text=text_data                                   
                                      )
                        )

        x_count = x_count + 1

        time.sleep(0.5)

    stream_mag.close()
    
if __name__ == "__main__":
    main()