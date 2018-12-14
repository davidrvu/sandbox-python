####LIBRERIAS#####

import time
import numpy as np
import pandas as pd
from pyspark.sql import functions as F
import matplotlib.pyplot as plt
from collections import OrderedDict
from pyspark.sql import SQLContext
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.util import MLUtils
from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.util import MLUtils
from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml import Pipeline 
from pyspark.ml import PipelineModel
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, PCA, CountVectorizer, StringIndexer
import re
import unicodedata
from pyspark.sql.functions import *
from pyspark.ml.tuning import TrainValidationSplit
from pyspark.sql.window import Window
from pyspark.mllib.linalg.distributed import IndexedRow, IndexedRowMatrix
from pyspark.ml.evaluation import RegressionEvaluator

######LECTURA DE DATOS###

data = sqlContext.sql("select * from parquet.`s3n://AKIAIBUPW24TNBAMHCMQ:Xzl%2FmjpEJzWDlCrpWqgb+af94ng4SbhiljWOKoVg@dev.exalitica.com/Ejemplos/BASE/`")
data.createOrReplaceTempView("data")


####TRABAJO FECHA#######
fecha = sqlContext.sql("""
select *, 
from_unixtime(unix_timestamp(FECHA,'yyyy-MM-dd'), 'E') as DIA_SEMANA,
from_unixtime(unix_timestamp(FECHA,'yyyy-MM-dd'), 'w') as SEMANA_ANO,
from_unixtime(unix_timestamp(FECHA,'yyyy-MM-dd'), 'dd') as FECHA_DIA,
from_unixtime(unix_timestamp(FECHA,'yyyy-MM-dd'), 'MM') as FECHA_MES,
from_unixtime(unix_timestamp(FECHA,'yyyy-MM-dd'), 'Y') as FECHA_ANO
from data """)
fecha.createOrReplaceTempView("fecha")

%sql
select * from fecha


#####CREACION TARGET MODELO####
baul1_ = sqlContext.sql("""
SELECT
FECHA,
HORA,
ID_CLIENTE,
ID_PRODUCTO,
MONTO,
CANTIDAD,
CASE 
WHEN FECHA_MES = 04  THEN 1  ELSE 0
END AS TARGET
FROM fecha
ORDER BY ID_CLIENTE, FECHA_MES
""")
baul1_.createOrReplaceTempView("baul1_")


target = sqlContext.sql("""
SELECT
ID_CLIENTE,
max(TARGET) as TARGET
FROM baul1_
GROUP BY ID_CLIENTE """)
target.createOrReplaceTempView("target")


###CREACION VARIABLES TEMPORALES#####

baul1 = sqlContext.sql("""
SELECT
ID_CLIENTE,
MAX(FECHA) AS FECHA_MAX_6M,
MIN(FECHA) AS FECHA_MIN_6M,
SUM(CANTIDAD) AS CANT_PRO_6M,
COUNT(DISTINCT(HORA)) AS CANT_VIS_6M,
SUM(MONTO) AS MONTO_6M
FROM baul1_
GROUP BY ID_CLIENTE """)
baul1.createOrReplaceTempView("baul1")


###ABT FINAL######
join2 = sqlContext.sql("""
select
a.*,
b.TARGET
from baul1 a left join target b on a.ID_CLIENTE = b.ID_CLIENTE
 """)
join2.createOrReplaceTempView("join2")

join3 = sqlContext.sql("""
SELECT *,
(datediff( FECHA_MAX_6M , FECHA_MIN_6M ) + 1 )as REC
FROM join2
""")
join3.createOrReplaceTempView("join3")


data3=sqlContext.sql(""" SELECT ID_CLIENTE, CAST(CANT_PRO_6M as double), 
CAST(CANT_VIS_6M as double), CAST(MONTO_6M as double),  CAST(REC as double), CAST(TARGET as double)
from join3""").cache()

display(data3)

##MUESTREO###

train, test, validation = data3.randomSplit((0.6, 0.3, 0.1))

#Construye un vector con las covariables que entraran al modelo
assembler = VectorAssembler(inputCols=data3.columns[1:4], outputCol="features")

train_l_f = assembler.transform(train).select("target","features").toDF("label", "features")
test_l_f = assembler.transform(test).select("target","features").toDF("label", "features")

display(train_l_f)

###ESTIMACION MODELO LOGISTICO SiMPLE#####

lr = LogisticRegression(maxIter=10, regParam=0.2)
pipeline = Pipeline(stages=[lr])
cvModel = pipeline.fit(train_l_f)

####Modelo complejo con grid y elastic parameter####################
lr = LogisticRegression(maxIter=10)
pipeline = Pipeline(stages=[lr])
paramGrid = ParamGridBuilder().addGrid(lr.regParam, [0,1,0.1]).addGrid(lr.elasticNetParam, [0,1,0.1]).build()
crossval = CrossValidator(estimator=pipeline,
                          estimatorParamMaps=paramGrid,
                          evaluator=BinaryClassificationEvaluator(),
                          numFolds=3)
cvModel = crossval.fit(train_l_f)


####EVALUACION MODELO#####
evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction")

prediction_train = cvModel.transform(test_l_f)
AUROC_train = evaluator.evaluate(prediction_train)

prediction_train.registerTempTable("prediction_train")


####MATRIZ DE CONFUSION#####

a = prediction_train.select("label","prediction").where("label=0 and prediction=0").count()
c = prediction_train.select("label","prediction").where("label=1 and prediction=0").count()
b = prediction_train.select("label","prediction").where("label=0 and prediction=1").count()
d = prediction_train.select("label","prediction").where("label=1 and prediction=1").count()

matriz_conf = {'pred_0':[a,c],'pred_1':[b,d]}
matriz_conf = pd.DataFrame(matriz_conf).reset_index()
matriz_conf['index']=['obs_0','obs_1']
matriz_conf

####SCORE###########

validation_l_f = assembler.transform(validation).select("target","ID_CLIENTE","features")

scorear = cvModel.transform(validation_l_f)
score = scorear.select("ID_CLIENTE", "probability").rdd.map(lambda row : [row[0],float(row[1][1])]).toDF([ "id", "score"])

score.createOrReplaceTempView("score")

%sql
select * from score
order by score DESC


###Decision Tree###
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

assembler = VectorAssembler(inputCols=data3.columns[1:4], outputCol="features")
data_index = assembler.transform(data3).select("target","features").toDF("label", "features")
labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(data_index)
featureIndexer =VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data_index)

(trainingData, testData) = data_index.randomSplit([0.7, 0.3])

dt = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures")

pipeline = Pipeline(stages=[labelIndexer, featureIndexer, dt])
model = pipeline.fit(trainingData)
predictions = model.transform(testData)
prediccion=predictions.select("prediction", "indexedLabel", "features")
prediccion.registerTempTable("prediccion")

testData.where("label=1").count()

###Matriz de confusión
a = prediccion.select("indexedLabel","prediction").where("indexedLabel=0 and prediction=0").count()
c = prediccion.select("indexedLabel","prediction").where("indexedLabel=1 and prediction=0").count()
b = prediccion.select("indexedLabel","prediction").where("indexedLabel=0 and prediction=1").count()
d = prediccion.select("indexedLabel","prediction").where("indexedLabel=1 and prediction=1").count()

matriz_conf = {'pred_0':[a,c],'pred_1':[b,d]}
matriz_conf = pd.DataFrame(matriz_conf).reset_index()
matriz_conf['index']=['obs_0','obs_1']
matriz_conf

###Random Forest#####
from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

##Se utilizan las mismas datas de entrenamineto anterior
rf = RandomForestClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures", numTrees=10)

# Convert indexed labels back to original labels.
labelConverter = IndexToString(inputCol="prediction", outputCol="predictedLabel",
                               labels=labelIndexer.labels)

# Chain indexers and forest in a Pipeline
pipeline = Pipeline(stages=[labelIndexer, featureIndexer, rf, labelConverter])

# Train model.  This also runs the indexers.
model = pipeline.fit(trainingData)

# Make predictions.
predictions = model.transform(testData)

prediccion=predictions.select("predictedLabel", "label", "features")

###Matriz de confusión
a = prediccion.select("label","predictedLabel").where("label=0 and predictedLabel=0").count()
c = prediccion.select("label","predictedLabel").where("label=1 and predictedLabel=0").count()
b = prediccion.select("label","predictedLabel").where("label=0 and predictedLabel=1").count()
d = prediccion.select("label","predictedLabel").where("label=1 and predictedLabel=1").count()

matriz_conf = {'pred_0':[a,c],'pred_1':[b,d]}
matriz_conf = pd.DataFrame(matriz_conf).reset_index()
matriz_conf['index']=['obs_0','obs_1']
matriz_conf






















