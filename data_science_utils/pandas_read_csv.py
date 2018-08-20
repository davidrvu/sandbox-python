# DAVIDRVU - 2018

from printDeb import printDeb
import pandas as pd
import sys

def pandas_read_csv(debug, file_input):
    printDeb(debug, "Abriendo archivo " + file_input + " con la función pandas_read_csv ... ")
    try:
        dataFrameIn = pd.read_csv(file_input, encoding="LATIN-1")
        #dataFrameIn = pd.read_csv(file_input, encoding="utf-8")
        #dataFrameIn = pd.read_csv(file_input, encoding="ISO-8859-1")
    except FileNotFoundError:
        print("\nERROR: El archivo " + file_input + " NO EXISTE. \n")
        sys.exit()
    return dataFrameIn