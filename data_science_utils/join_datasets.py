# DAVIDRVU - 2017
# SE ASUME QUE EL(LOS) ARCHIVO(S) DE ENTRADA (.csv) TIENEN HEADERS Y EL(LOS) ARCHIVO(S) DE SALIDA TIENEN LOS MISMOS HEADERS

from pandas_read_csv import pandas_read_csv
from pandas_write_csv import pandas_write_csv
import pandas as pd
import sys

def join_datasets(file_train,file_test, file_out, final_sort, header_labels):
    print("\n----> START join_datasets")

    dataFrame_train = pandas_read_csv(file_train)
    dataFrame_test  = pandas_read_csv(file_test)    

    dataFrameFinal  = pd.concat([dataFrame_train, dataFrame_test], axis=0)

    if final_sort == True:
        print("sorting by " + header_labels + " ...")
        dataFrameFinal.sort_values(by=[header_labels], inplace = True)

    #print("dataFrameFinal = ")
    #print(dataFrameFinal)

    pandas_write_csv(dataFrameFinal, file_out)

    print("----> END join_datasets\n")