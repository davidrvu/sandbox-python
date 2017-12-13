import pandas as pd

def pandas_read_xlsx(file_input, sheet_name):
    print("Abriendo archivo " + file_input + " con la función pandas_read_xlsx ... ")
    try:
        dataFrameIn = pd.read_excel(file_input, sheet_name=sheet_name)
    except FileNotFoundError:
        print("\nERROR: El archivo " + file_input + " NO EXISTE. \n")
        sys.exit()
    return dataFrameIn