# DAVIDRVU - 2017
import os
import pandas as pd

def pandas_write_csv(dataFrame_In, file_name_full):
    print("\n----> START pandas_write_csv")

    directory = os.path.dirname(file_name_full)
    if not os.path.exists(directory): # Si el directorio no existe, entonces se crea
        print("Como el directorio no existe, entonces se crea: " + directory)
        os.makedirs(directory)

    print("Guardando archivo " + file_name_full + " ... ")
    dataFrame_In.to_csv(file_name_full, index=False)

    print("----> END pandas_write_csv\n")