# DAVIDRVU - 2018

# FUENTE: https://github.com/nicodv/kmodes

# BIBLIOGRAFIA: 
#		[HUANG97]	(1, 2) Huang, Z.: Clustering large data sets with mixed numeric and categorical values, Proceedings of the First Pacific Asia Knowledge Discovery and Data Mining Conference, Singapore, pp. 21-34, 1997.
#		[HUANG98]	Huang, Z.: Extensions to the k-modes algorithm for clustering large data sets with categorical values, Data Mining and Knowledge Discovery 2(3), pp. 283-304, 1998
#		[CAO09]  	Cao, F., Liang, J, Bai, L.: A new initialization method for categorical data clustering, Expert Systems with Applications 36(7), pp. 10223-10228., 2009.

# k-modes is used for clustering categorical variables. 
# It defines clusters based on the number of matching categories between data points. 
# (This is in contrast to the more well-known k-means algorithm, which clusters numerical data based on Euclidean distance.)
# The k-prototypes algorithm combines k-modes and k-means and is able to cluster mixed numerical / categorical data.

from kmodes.kmodes import KModes
import numpy as np
import os
import sys

sys.path.insert(0, '../../data_science_utils')
from pandas_read_csv import pandas_read_csv
from pandas_write_csv import pandas_write_csv
from printDeb import printDeb


def kmodes_func(debug, num_clusters, features_headers, input_filename, output_filename):
    printDeb(debug, "\n----> START " + str(sys._getframe().f_code.co_name) )

    printDeb(debug, " READING INPUT FILE")
    df_in = pandas_read_csv(debug, input_filename)

    df_features = df_in[features_headers]
    print("df_features = ")
    print(df_features)

    features = df_features.as_matrix()
    print("features = ")
    print(features)

    num_clusters_len = len(num_clusters)
    for i in range(0, num_clusters_len):
        current_n_clust = num_clusters[i]
        print("current_n_clust = " + str(current_n_clust))
        kmodes_huang = KModes(n_clusters=current_n_clust, init='Huang', verbose=1)
        kmodes_huang.fit(features)

        print("kmodes_huang.labels_ = ")
        print(kmodes_huang.labels_)




    sys.exit()


    syms = np.genfromtxt('stocks2.csv', dtype=str, delimiter=',')[:, 0]
    features = np.genfromtxt('stocks2.csv', dtype=object, delimiter=',')[:, 1:]



    print("syms = ")
    print(syms)
    print("features = ")
    print(features)


    #kproto = KPrototypes(n_clusters=4, init='Cao', verbose=3, n_init=1)
    #kproto = KPrototypes(n_clusters=2, init='Cao', verbose=4, max_iter = 100)
    kproto = KPrototypes(n_clusters=2, init='Huang', n_init = 1, verbose=True)

    #clusters = kproto.fit_predict(features, categorical=[1, 2])
    #clusters = kproto.fit_predict(features, categorical=[0, 1])
    #clusters = kproto.fit_predict(features, categorical=[1])



    kmodes_huang = KModes(n_clusters=2, init='Huang', verbose=1)
    kmodes_huang.fit(features)

    print("kmodes_huang.labels_ = ")
    print(kmodes_huang.labels_)






    print("clusters = ")
    print(clusters)


    # Print cluster centroids of the trained model.
    print(kproto.cluster_centroids_)
    # Print training statistics
    print(kproto.cost_)
    print(kproto.n_iter_)

    for s, c in zip(syms, clusters):
        print("Symbol: {}, cluster:{}".format(s, c))





    printDeb(debug, "----> END " + str(sys._getframe().f_code.co_name) + "\n")

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~ MAIN KMODES -> CLUSTERING ONLY CATEGORICAL VARIABLES ~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    ######################################
    ## PARAMETERS 
    ######################################
    debug = 1

    num_clusters     = [2, 3, 4]
    features_headers = ["Feature_1", "Feature_2"]
    input_filename   = "dataset_only_categ.csv"
    output_filename  = "dataset_only_categ_OUT.csv"
    ######################################

    kmodes_func(debug, num_clusters, features_headers, input_filename, output_filename)


    print("DONE!")

if __name__ == "__main__":
    main()