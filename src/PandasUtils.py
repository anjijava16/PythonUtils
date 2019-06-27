from pyspark import *
from pyspark.sql import SparkSession
import pandas as pd;
import os


conf = SparkConf()
os.environ["SPARK_HOME"] = "F:/Python_Dev/spark-2.1.1-bin-hadoop2.7"
print("Starting Before Main Method here")
# spark = SparkSession.builder().appName("Spark SQL basic example").master("local[*]").getOrCreate()
# spark = SparkSession.builder.master("local[*]").appName("Data cleaning").getOrCreate(conf)
spark = SparkSession.builder.master("local[*]").getOrCreate()
print(type(spark))
print("welcome to Main")
dataFrame=spark.read.option("header", "true").csv("F:/Works/pandas/py_master/pandas/2_dataframe_basics/weather_data.csv")
dataFrame.printSchema()
dataFrame.show()
pdf = dataFrame.toPandas()
print("One PDF",pdf)
print("============================================= Start Here ============== ")
for row in pdf.iterrows():
                print(row[1]['day'])

print("============================================= End Here  ================")