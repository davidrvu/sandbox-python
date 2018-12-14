###Cargar librerias

from pyspark.sql.functions import col, expr, when
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
import numpy as np
import scipy.sparse as sps
from pyspark.mllib.stat import Statistics
from pyspark.mllib.fpm import FPGrowth


###Generación de funciones
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf
removeChars1 = udf(lambda x: x.replace("]",""), StringType())
removeChars2 = udf(lambda x: x.replace("[",""), StringType())
removeChars3 = udf(lambda x: x.replace(" ",""), StringType())

file_location = file_location = 's3n://AKIAIE5CQXJUMHM36OKQ:xHYvcrTlw78NBr53JZr0AArcblDDIzUzQXx5aA9N@bootcamp-deloitte/Tran-sample/Taller2.csv'
file_type = "csv"

# CSV options
infer_schema = "true"
first_row_is_header = "false"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
data = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location).toDF("FECHA","HORA","ID_CLIENTE","ID_PRODUCTO","MONTO","CANTIDAD")

display(data)

data.printSchema()
data.select("ID_CLIENTE").distinct().count()

fuente2 = data.select("ID_PRODUCTO", "FECHA", "ID_CLIENTE").where("ID_CLIENTE > 0")

from pyspark.sql.functions import collect_list, col
 
transactions = fuente2.groupBy(["ID_CLIENTE","FECHA"])\
      .agg(collect_list("ID_PRODUCTO").alias("ID_PRODUCTO"))\
      .rdd\
      .map(lambda fuente2: fuente2.ID_PRODUCTO)


transactions.collect()

unique = transactions.map(lambda x: list(set(x))).cache()
t=FPGrowth.train(unique, minSupport=0.0001,numPartitions=1)

result1 = t.freqItemsets()
result1.count()

schema1 = StructType([
StructField("BOLETA", StringType(), True),  
StructField("FREC", LongType(), True)])
df = sqlContext.createDataFrame(result1, schema1)
df.registerTempTable("prueba")


%sql
select * from prueba

tj = df.rdd
tj1 = tj.map(lambda row : ([row[0], row[1], row[0].count(',')]))

schema3 = StructType([
StructField("ASOC", StringType(), True),  
StructField("FREQ", LongType(), True),
StructField("CUENTA", StringType(), True)])
df1 = sqlContext.createDataFrame(tj1, schema3)

df1.show(100,False)

df1=df1.withColumn("ASOC", removeChars2(col("ASOC"))).withColumn("ASOC", removeChars1(col("ASOC")))


aux1=df1.where("CUENTA = 0")
aux2=df1.where("CUENTA = 1")

aux1.registerTempTable("pruebaa")

aux1 = sqlContext.sql("""
                      select 
                      substr(ASOC,2,32) as ASOC, 
                      FREQ, 
                      CUENTA 
                      from pruebaa""")

aux1.show(100,False)

aux3 = aux2.rdd.map(lambda x: [x[0].split(",")[0], x[0].split(",")[1], x[1] , x[2]])

schema4 = StructType([
StructField("PREDEC", StringType(), True),  
StructField("CONSEC", StringType(), True),
StructField("SOP_CONJ", LongType(), True),
StructField("CUENTA", StringType(), True)])

aux4 = sqlContext.createDataFrame(aux3, schema4)

aux4.show(100,False)

aux5 = aux4.drop("CUENTA")

aux6 = aux5.join(aux1, aux5.PREDEC == aux1.ASOC, 'left')
aux6.show()

aux6 = aux6.drop("ASOC").drop("CUENTA")
aux6.show()

aux6 = aux6.select(col("PREDEC"), col("CONSEC"), col("SOP_CONJ"), col("FREQ").alias("SOP_PREDEC")).withColumn("CONSEC", removeChars3(col("CONSEC")))

aux7 = aux6.join(aux1, aux6.CONSEC == aux1.ASOC, 'left')
aux7 = aux7.drop("ASOC").drop("CUENTA")

aux7.show()

aux7 = aux7.select(col("PREDEC"), col("CONSEC"), col("SOP_CONJ"), col("SOP_PREDEC"), col("FREQ").alias("SOP_CONSEC"))

n = transactions.count()
n

aux7 = aux7.withColumn("B/A", aux7[2]/n).withColumn("A", aux7[3]/n).withColumn("B", aux7[4]/n)
aux8 = aux7.withColumn("lift",(aux7[5]/(aux7[6]*aux7[7])))

asoc_lift = aux8.select("PREDEC", "CONSEC", "B/A", "A", "B", "lift")
asoc_lift = asoc_lift.sort(asoc_lift.lift.desc())
asoc_lift.registerTempTable("lift")

%sql
select * from lift
order by B/A desc
limit 10

%sql
select * from lift
order by lift desc
limit 10

%sql
select * from lift
order by lift asc
limit 10
