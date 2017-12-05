import pandas as pd

def pandas_read_csv(file_input):
    print("Abriendo archivo " + file_input + " con la función pandas_read_csv ... ")
    try:
        dataFrameIn = pd.read_csv(file_input, encoding="ISO-8859-1")
    except FileNotFoundError:
        print("\nERROR: El archivo " + file_input + " NO EXISTE. \n")
        sys.exit()
    return dataFrameIn