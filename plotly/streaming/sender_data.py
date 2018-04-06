# DAVIDRVU 2018

import plotly
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import datetime
import time


def main():
    print("SENDER DATA")

    stream_token = 'AAABBB'

    stream = plotly.plotly.Stream(stream_token)
    stream.open()

    y_data = 0
    while True:
        
        stream.write({'x': datetime.datetime.now(), 'y': y_data})
        y_data = y_data + 1
        time.sleep(0.1) # delay between stream posts

if __name__ == "__main__":
    main()