import pandas as pd;
import pyspark as ps;
df=pd.read_csv("F:/works/pandas/py_master/pandas/1_intro/nyc_weather.csv")
print(df['Temperature'].max())

