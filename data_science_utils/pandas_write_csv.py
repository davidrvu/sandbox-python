# DAVIDRVU - 2018

from print_time import print_time
from printDeb import printDeb
import os
import pandas as pd
import time

def pandas_write_csv(debug, dataFrame_In, file_name_full, **key_param):
    printDeb(debug, "\n----> START pandas_write_csv")

    time_ini_tocsv = time.time()
    directory = os.path.dirname(file_name_full)
    print("directory = " + str(directory))
    if directory != "":
        if not os.path.exists(directory): # Si el directorio no existe, entonces se crea
            printDeb(debug, "Como el directorio no existe, entonces se crea: " + directory)
            os.makedirs(directory)

    success = False
    while not success:
        try:
            printDeb(debug, "Guardando archivo " + file_name_full + " ... ")
            if ('na_rep' in key_param):
                dataFrame_In.to_csv(file_name_full, index=False, na_rep=key_param['na_rep'], encoding="latin-1")
                #dataFrame_In.to_csv(file_name_full, index=False, na_rep=key_param['na_rep'], encoding="utf-8")
            else:
                dataFrame_In.to_csv(file_name_full, index=False, encoding="latin-1")
                #dataFrame_In.to_csv(file_name_full, index=False, encoding="utf-8")
            success = True
        except Exception:
            print_time("        WARNING: Close the file!!!")
            time.sleep(1)

    time_fin_tocsv = time.time()
    printDeb(debug, "Elapsed time to_csv = " + str(round(time_fin_tocsv - time_ini_tocsv, 4)) + "[s]." ) 

    printDeb(debug, "----> END pandas_write_csv\n")