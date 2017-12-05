# DAVIDRVU - 2017
# SE ASUME QUE EL(LOS) ARCHIVO(S) DE ENTRADA (.csv) TIENEN HEADERS Y EL(LOS) ARCHIVO(S) DE SALIDA TIENEN LOS MISMOS HEADERS
# El PORCENTAJE del conjunto training se respeta para cada CLASE por separado (stratify)!
from split_datasets import split_datasets

def main():
    print("\n----> START main_split_datasets")

    split_datasets("data_fake/all1.csv", 0.80, "CLASES", final_sort = True)

    print("\n----> END   main_split_datasets")

if __name__ == "__main__":
    main()