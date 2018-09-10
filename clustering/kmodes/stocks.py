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

import numpy as np
from kmodes.kprototypes import KPrototypes
from kmodes.kmodes import KModes
import sys

# stocks with their market caps, sectors and countries
#syms = np.genfromtxt('stocks.csv', dtype=str, delimiter=',')[:, 0]
#features = np.genfromtxt('stocks.csv', dtype=object, delimiter=',')[:, 1:]

syms = np.genfromtxt('stocks2.csv', dtype=str, delimiter=',')[:, 0]
features = np.genfromtxt('stocks2.csv', dtype=object, delimiter=',')[:, 1:]

#features[:, 0] = features[:, 0].astype(float)

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

# TODOTODO: SEPARAR EN ARCHIVO MIXTO (Categorica y continua) -> kproto y sólo CATEGORICA -> kmodes
sys.exit()

print("clusters = ")
print(clusters)


# Print cluster centroids of the trained model.
print(kproto.cluster_centroids_)
# Print training statistics
print(kproto.cost_)
print(kproto.n_iter_)

for s, c in zip(syms, clusters):
    print("Symbol: {}, cluster:{}".format(s, c))