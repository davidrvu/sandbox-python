# DAVIDRVU 2018

from plotly.graph_objs import *
from scipy.optimize import curve_fit
from scipy.stats import norm
from scipy.stats import skewnorm
import datetime as dt
import math
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import plotly.plotly as py
import sqlite3

def wind_speed_generation():

    windVal = []
    windError = []
    windOrientation = []
    prevVal = 20
    prevOrientation = np.random.uniform(0, 360)
    for i in range(0, 86400):
        windVal.append(abs(np.random.normal(prevVal, 2, 1)[0]))
        windError.append(abs(np.random.normal(round(prevVal/10), 1)))
        if(i % 100 == 0):
            windOrientation.append(np.random.uniform(prevOrientation-50, prevOrientation+50))
        else:
            windOrientation.append(np.random.uniform(prevOrientation-5, prevOrientation+5))
        if(round(windVal[-1]) > 45):
            prevVal = int(math.floor(windVal[-1]))
        elif(round(windVal[-1]) < 10):
            prevVal = int(math.ceil(windVal[-1]))
        else:
            prevVal = int(round(windVal[-1]))
        prevOrientation = windOrientation[-1]


    df = pd.DataFrame.from_dict({
                                 'Speed': windVal,
                                 'SpeedError': windError,
                                 'Direction': windOrientation
                                })

    now = dt.datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour

    totalTime = (hour * 3600) + (minute * 60) + (sec)

    ####################################################
    ## WRITE
    ####################################################
    connex = sqlite3.connect("wind-data.db")  # Opens file if exists, else creates file
    cur = connex.cursor()

    df.to_sql(name='Wind', con=connex)

    ####################################################
    ## READ
    ####################################################

    #con = sqlite3.connect("wind-data.db")
    #df = pd.read_sql_query("SELECT * from Wind where rowid > "+ str(totalTime-200) + " AND rowid < " + str(totalTime) + ";" , con)


def main():
    wind_speed_generation()

if __name__ == "__main__":
    main()