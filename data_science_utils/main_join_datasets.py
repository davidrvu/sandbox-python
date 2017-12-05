# DAVIDRVU - 2017
# SE ASUME QUE EL(LOS) ARCHIVO(S) DE ENTRADA (.csv) TIENEN HEADERS Y EL(LOS) ARCHIVO(S) DE SALIDA TIENEN LOS MISMOS HEADERS

from join_datasets import join_datasets

def main():
    print("\n----> START main_join_datasets")

    #join_datasets("data_fake/all1_train.csv","data_fake/all1_test.csv", "data_fake/all1_joined.csv",final_sort = True, header_labels="CLASES")

    #join_datasets("C:\\davidrvu\\data_bases\\dbpedia\\train.csv","C:\\davidrvu\\data_bases\\dbpedia\\test.csv", "C:\\davidrvu\\data_bases\\dbpedia\\dbpedia_all.csv",final_sort = True, header_labels="class")

    join_datasets("C:\\davidrvu\\data_bases\\dbpedia\\train_small.csv","C:\\davidrvu\\data_bases\\dbpedia\\test_small.csv", "C:\\davidrvu\\data_bases\\dbpedia\\dbpedia_all_small.csv",final_sort = True, header_labels="class")

    print("\n----> END   main_join_datasets")

if __name__ == "__main__":
    main()