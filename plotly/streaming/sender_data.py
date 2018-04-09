# DAVIDRVU 2018

# SOURCE: https://stackoverflow.com/questions/28161244/how-to-create-two-y-axes-streaming-plotly

from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis
import datetime
import numpy as np
import plotly.plotly as py # plotly library
import sys
import time


def main():
    print("SENDER DATA")

    stream_token_temperature = 'aghuvyozmm'
    stream_token_humidity    = '5mfgh2l9jl'

    stream_temperature = py.Stream(stream_token_temperature)
    stream_temperature.open()

    stream_humidity = py.Stream(stream_token_humidity)
    stream_humidity.open()

    print("Starting main loop ...")
    x_count   = 0 
    freq_temp = 10
    freq_hum  = 5
    Fs        = 100

    temp_min = -5
    temp_max = 35

    humidity_min = 10
    humidity_max = 30

    temp_amp = (temp_max - temp_min)/2.0
    humi_amp = (humidity_max - humidity_min)/2.0

    temp_mean = np.mean([temp_max, temp_min])
    humi_mean = np.mean([humidity_max, humidity_min])

    print("temp_amp  = " + str(temp_amp))
    print("humi_amp  = " + str(humi_amp))

    print("temp_mean = " + str(temp_mean))
    print("humi_mean = " + str(humi_mean))

    while(True):

        temp     = round((temp_amp * np.sin(2 * np.pi * freq_temp * x_count / Fs) + 0        ) + temp_mean , 3)
        humidity = round((humi_amp * np.sin(2 * np.pi * freq_hum  * x_count / Fs) + (np.pi/2)) + humi_mean , 3) 

        time_now = datetime.datetime.now()

        print(str(time_now) + " | Temp = " + str(temp) + " | humidity = " + str(humidity))

        stream_temperature.write({'x': time_now, 'y': temp })
        stream_humidity.write({'x': time_now, 'y': humidity })

        x_count = x_count + 1

        time.sleep(2)

    stream_temperature.close()
    stream_humidity.close()
    
if __name__ == "__main__":
    main()