Ctrl+Enter : Next Row in Notebook

import pandas as pd

df=pd.read_csv("newyourk.csv")

df['Temerature'].max()

df['EST'][df['Events']=='Rain'] //Here  2 Dispaly EST and equals to Rain also

df['WindSpeedMPH'].mean()

df.fillna(0,inplace=True)
df['WindSpeedMPH'].mean()


========================

weather_data={
	'day':['1/2017','2/2018'],
	'temp':[32,33],
	'windspeed':[5,4],
	'events':['rain','sunny']
}
df=pd.DataFrame(weather_date)

df.shape()
Ans:(6,4)
6 is Rows
4 is Columns

$ rows,columns=df.shape
$ rows ans:6
$ columns ans:4


df.head
df.head(2)

df.tail()  //Last 5 rows

df.tail(1) 
//Last one Row

df[2:5]

df[:]
  (OR)
df


df.columns

df.day # Day Columns

df.event # DF Events Info Column
 (OR)
df['event']

type(df['event'])

df['event','day'] (Both will print below)

df['event','day','temperature']

df

# Max Temparatur

df['temparature'].max() (Ctrl+Enter OR some icon in notebook)

df['temparature'].min()
df['temparature'].std()
df['temparature'].mean()
df.describe()


df(df.temperature>=32)

df[df.temperature==df.temperature.max()]

df[df.temeprature==df['temperature'].max()]

df[['day','tempeature']][df.temeprature==df['temperature'].max()]

======================================
df.index
df.set_index('day',inplace=true)

df.loc['1/3/2017']

======================================
df.reset_index(inplace=True)
df

======================================
df.set_index('event',inplace=True)
df.loc['Snow']

======================

Using CSV
import pandas as pd
df=pd.read_csv("weather.csv")

//Create a Data Frame from Excel File

df1=pd.read_excel("weather.xlsx","Sheet1");//Sheet name also mentioned
[df1]

create Data Frame using Python Dicrotry

weahter_data={
	'day':['10','11'],
	'event':['rain','sunny']

}
df3=pd.DataFrame(weather_data)

------------------------------------------------------------
List Of Tuplea must be mentioned columns info
//From Tuple 
weahter_data={
	'day':['10','11'],
	'event':['rain','sunny']

}

------------------------------------------------------------

weather_Data=[
{'day':'1/1/17','temp':32,'event':'snny'},
{'day':'1/1/17','temp':32,'event':'snny'}
]

df5=pd.DataFrame(weather_Data)

import pandas as pd

stats = {
    'Month': ['Jan', 'Feb', 'March', 'April'],
    'Expenses': [2350, 3400, 2700, 2200],
    'Income': [4000, 4000, 4000, 4000]
}

df = pd.DataFrame(stats)
# df = df.set_index('Month')
print(df.Month)

=====================================
Read CSV

import pandas as pd
df=pd.read_csv("stock_data.csv")

df=pd.read_csv("stock_data.csv",skiprows=1)
df=pd.read_csv("stock_data.csv",header=1)

df=pd.read_csv("stock_data.csv",header=None)

df=pd.read_csv("stock_data.csv",skiprows=1,names=['ticker','eps','revenue','price','people'])



df=pd.read_csv("stock_data.csv",nrows=3)
df=pd.read_csv("stokc.csv",na_values=["not avilable","n.a."])
df=pd.read_csv("stokc.csv",na_values={
	'eps':["not avialable","n.a."],
	'revenue':["not available","n.a."],
	'people':["not avialble","n.a."]
})
df

# Write into CSV using Pandas
df.to_csv('new.csv')
df.to_csv('new.csv',index=False)
df.columns
df.to_csv('new.csv',columns=['tickets','eps'],index=False)
df.to_csv('new.csv',header=False)

//Writing Excel

df=pd.read_excel("stock_data.xlsx","Sheet1")
def convert_people_cell(cell):
	if cell=="n.e.":
		return 'Sam Walton'
	return cell	
df=pd.read_excel("stock_data.csv","sheet1",converters={
   'people':cpmvert_people_cell,
   'eps':convert_eps_cell
})

def convert_eps_cell(cell):
	if cell=="not available":
		return None
	return cell
pd.to_excel("news.xlsx",shee_name="stocks",sheet_name="stocks",startrow=1,start)

with pd.ExcelWriter("stocks.xlsx") as writer:
     df_stocks.to_excel(writer,sheet_nam="stocks")
     df_weather.to_excel(writer,sheet_name="weather")	
		
	   



df4=pd.DataFrame(weather_Data,columns=['day','events'])