# DAVIDRVU - 2017
# SE ASUME QUE EL(LOS) ARCHIVO(S) DE ENTRADA (.csv) TIENEN HEADERS Y EL(LOS) ARCHIVO(S) DE SALIDA TIENEN LOS MISMOS HEADERS
# El PORCENTAJE del conjunto training se respeta para cada CLASE por separado (stratify)!

from get_dir_file_ext import get_dir_file_ext
from pandas_read_csv import pandas_read_csv
from pandas_write_csv import pandas_write_csv
from sklearn.model_selection import train_test_split
import pandas as pd
import sys

def split_datasets(file_input, train_perc, header_labels, final_sort):
    print("\n----> START split_datasets")

    dataFrameIn = pandas_read_csv(file_input)
    dataFrameIn_rows = dataFrameIn.shape[0]

    # Se verifica si la columna header_labels existe en el dataFrame
    if header_labels in dataFrameIn.columns:
        print("header_labels = " + header_labels + ", si exite en el dataFrameIn")
    else:
        print("ERROR: header_labels = " + header_labels + ", NO EXISTE en el dataFrameIn")
        sys.exit()

    [directory, filename_in_base, ext] = get_dir_file_ext(file_input)

    file_train = directory + "//" + filename_in_base + "_train.csv"
    file_test  = directory + "//" + filename_in_base + "_test.csv"

    print("train_perc       = " + str(train_perc))
    print("file_train       = " + file_train)
    print("file_test        = " + file_test)
    print("dataFrameIn_rows = " + str(dataFrameIn_rows))

    print("train_test_split (stratify by header_labels = " + header_labels + ") ...")
    df_train, df_test = train_test_split(dataFrameIn, train_size=train_perc, stratify=dataFrameIn[header_labels])

    if final_sort == True:
        print("sorting by " + header_labels + " ...")
        df_train.sort_values(by=[header_labels], inplace = True)
        df_test.sort_values(by=[header_labels],  inplace = True)

    #print("-------------------------------------------------")
    #print("df_train = ")
    #print(df_train)
    #print("-------------------------------------------------")
    #print("df_test = ")
    #print(df_test)
    #print("-------------------------------------------------")

    df_train_rows = df_train.shape[0]
    df_test_rows  = df_test.shape[0]
    ########################################################################
    ##   RESUMEN (Cuantas muestras por clase hay en cada archivo)
    ########################################################################
    print("-------------------------------------------------")
    print("---> TRAINING SET - LABELS FREQUENCY: " + str(round(train_perc,3)) + " ("+str(df_train_rows)+" rows)")
    print(df_train[header_labels].value_counts())
    print("-------------------------------------------------")
    print("---> TEST SET     - LABELS FREQUENCY: " + str(round(1-train_perc,3)) + " ("+str(df_test_rows)+" rows)")
    print(df_test[header_labels].value_counts())
    print("-------------------------------------------------")
    pandas_write_csv(df_train, file_train)
    pandas_write_csv(df_test, file_test)

    print("----> END split_datasets\n")