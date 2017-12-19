# DAVIDRVU - 2017
# SE ASUME QUE EL(LOS) ARCHIVO(S) DE ENTRADA (.csv) TIENEN HEADERS Y EL(LOS) ARCHIVO(S) DE SALIDA TIENEN LOS MISMOS HEADERS
# El PORCENTAJE del conjunto training se respeta para cada CLASE por separado (stratify)!

from get_dir_file_ext import get_dir_file_ext
from pandas_read_csv import pandas_read_csv
from pandas_write_csv import pandas_write_csv
from sklearn.model_selection import train_test_split
import collections
import pandas as pd
import sys

def split_datasets(file_input, train_perc, header_labels, min_samples, final_sort):
    print("\n----> START split_datasets")

    dataFrameIn = pandas_read_csv(file_input)
    dataFrameIn_rows = dataFrameIn.shape[0]

    # Se verifica si la columna header_labels existe en el dataFrame
    if header_labels in dataFrameIn.columns:
        print("header_labels = " + header_labels + ", si exite en el dataFrameIn")
    else:
        print("ERROR: header_labels = " + header_labels + ", NO EXISTE en el dataFrameIn")
        sys.exit()

    #################################################################
    # FILTRO DE MUESTRAS POR CLASE: Se asegura un mínimo numero de muestras (min_samples) por clase. De lo contrario se eliminan los registros!
    #################################################################
    print("min_samples = " + str(min_samples))

    allLabels      = dataFrameIn[header_labels].tolist()

    allLabels_freq                 = collections.Counter(allLabels)
    allLabels_freq_sorted          = sorted(allLabels_freq.items(), key=lambda item: (-item[1], item[0]))
    allLabels_freq_sorted_dict     = collections.OrderedDict(allLabels_freq_sorted)
    allLabels_freq_sorted_dict_len = len(allLabels_freq_sorted_dict)

    print(allLabels_freq_sorted_dict)
    print("allLabels_freq_sorted_dict_len = " + str(allLabels_freq_sorted_dict_len))

    labels_deleted     = dict((k, v) for k, v in allLabels_freq_sorted_dict.items() if v < min_samples)

    print("labels_deleted = ")
    print(labels_deleted) # Se muestran las etiquetas de registros que se van a eliminar y su frecuencia.
 
    labels_deleted_len = len(labels_deleted)
    print("labels_deleted_len = " + str(labels_deleted_len))

    labels_deleted_list = list(labels_deleted.keys())
    total_deleted_reg   = sum(list(labels_deleted.values()))

    dataFrameFiltered   = dataFrameIn[~dataFrameIn[header_labels].isin(labels_deleted_list)] # FILTRO

    dataFrameFiltered_rows = dataFrameFiltered.shape[0]
    print("dataFrameIn_rows       = " + str(dataFrameIn_rows))
    print("total_deleted_reg      = " + str(total_deleted_reg))
    print("dataFrameFiltered_rows = " + str(dataFrameFiltered_rows))

    #################################################################
    # Se setean directorios de archivos de salida
    #################################################################

    [directory, filename_in_base, ext] = get_dir_file_ext(file_input)

    file_train   = directory + "//" + filename_in_base + "_" + header_labels + "_train.csv"
    file_test    = directory + "//" + filename_in_base + "_" + header_labels + "_test.csv"

    print("train_perc       = " + str(train_perc))
    print("file_train       = " + file_train)
    print("file_test        = " + file_test)

    #################################################################
    # Se realiza la separación de dataFrames
    #################################################################   

    print("train_test_split (stratify by header_labels = " + header_labels + ") ...")
    df_train, df_test = train_test_split(dataFrameFiltered, train_size=train_perc, stratify=dataFrameFiltered[header_labels])

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
    train_set_counts = df_train[header_labels].value_counts()
    print(train_set_counts)
    print("-------------------------------------------------")
    print("---> TEST SET     - LABELS FREQUENCY: " + str(round(1-train_perc,3)) + " ("+str(df_test_rows)+" rows)")
    test_set_counts  = df_test[header_labels].value_counts()
    print(test_set_counts)
    print("-------------------------------------------------")
    pandas_write_csv(df_train, file_train)
    pandas_write_csv(df_test, file_test)

    print("----> END split_datasets\n")

    return [train_set_counts, test_set_counts]