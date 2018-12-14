#Cargar librerias
from pyspark.sql.functions import col, expr, when
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
from pyspark.mllib.stat import Statistics
from pyspark.ml.feature import QuantileDiscretizer


#Ruta del archivo
file_location = 's3n://AKIAIE5CQXJUMHM36OKQ:xHYvcrTlw78NBr53JZr0AArcblDDIzUzQXx5aA9N@bootcamp-deloitte/Tran-sample/Taller2.csv'
file_type = "csv"

# formato del archivo
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

# Lectura del archivo.
data = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location).toDF("FECHA","HORA","ID_CLIENTE","ID_PRODUCTO","MONTO","CANTIDAD").cache()

data.registerTempTable("data")


###Cálculo inicial de variables a partir de la data##
###Recencia:Intervalo de tiempo entre la primera y la última compra

temporal01 = sqlContext.sql("""
SELECT
ID_CLIENTE,
DATEDIFF(MAX(CAST(FECHA AS DATE)),MIN(CAST(FECHA AS DATE))) AS FECHA_PROM,
COUNT(DISTINCT(HORA)) AS CANT_VIS,
SUM(MONTO) AS MONTO
FROM data
GROUP BY ID_CLIENTE
 """)
temporal01.registerTempTable("temp01")


###Imputación Recencia 0 por valor máximo###

temporal02 = sqlContext.sql("""
SELECT *,
CASE 
WHEN FECHA_PROM = 0 THEN 180
ELSE FECHA_PROM
END AS REC
FROM temp01
 """)
temporal02.registerTempTable("temp02")

###Quitilización variables Recencia, Frecuencia y Monto###

df_iter = temporal02.drop("FECHA_PROM")
nueva_lista = ["REC","CANT_VIS","MONTO"]
nueva_lista_salida = ["R","F","M"]
for i in range(0,3):
  discretizer = QuantileDiscretizer(numBuckets=5, inputCol=nueva_lista[i], outputCol=nueva_lista_salida[i])
  result = discretizer.fit(df_iter).transform(df_iter)
  df_iter = result

 ##CALCULO FINAL SCORE RFM######

RFM = df_iter.withColumn("R",(df_iter["R"]+1)).withColumn("F",(df_iter["F"]+1)).withColumn("M",(df_iter["M"]+1))
RFM.registerTempTable("RFM")


RFM_aux=sqlContext.sql("""
SELECT *,
CASE 
WHEN R = 1 THEN 5
WHEN R = 2 THEN 4
WHEN R = 3 THEN 3
WHEN R = 4 THEN 2
WHEN R = 5 THEN 1
END AS R1
FROM RFM
 """)
RFM_aux.registerTempTable("RFM_aux")

RFM1 = RFM_aux.withColumn("RFM",RFM_aux["R1"] * RFM_aux["F"]* RFM_aux["M"]) 
RFM1.registerTempTable("dt1")

%sql
SELECT AVG(RFM) AS Promedio,stddev(RFM) AS DESVIACION, MIN(RFM) AS MINIMO_PUNTAJE,MAX(RFM) AS MAXIMO_PUNTAJE
FROM dt1

%sql
SELECT SEGMENTO,AVG(RFM) AS Promedio,stddev(RFM) AS DESVIACION, MIN(RFM) AS MINIMO_PUNTAJE,MAX(RFM) AS MAXIMO_PUNTAJE
FROM (SELECT *, 
CASE 
WHEN RFM <27 THEN 'BAJO'
WHEN RFM >=27 AND RFM <48 THEN 'MEDIO'
WHEN RFM >=48 AND RFM <125 THEN 'ALTO'
WHEN RFM = 125 THEN 'MAXIMO'
END AS SEGMENTO
FROM dt1
)
GROUP BY SEGMENTO


%sql
select SEGMENTO, COUNT(DISTINCT ID_CLIENTE) AS CUENTA
FROM 
(SELECT *, 
CASE 
WHEN RFM <27 THEN 'BAJO'
WHEN RFM >=27 AND RFM <48 THEN 'MEDIO'
WHEN RFM >=48 AND RFM <125 THEN 'ALTO'
WHEN RFM = 125 THEN 'MAXIMO'
END AS SEGMENTO
FROM dt1
)
GROUP BY SEGMENTO