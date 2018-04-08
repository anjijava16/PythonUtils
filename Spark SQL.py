


pspark :==>
--master yarn
--conf spark.ui.port=12562


// Overwrite
pyspark --help


Memory 120GB  (160GB)
VCores: 30   (42)


By Default 2 execorts

from pyspark import SparkConf,SparkContext
conf=SparkConf().setMaster("yarn").setAppName("Testing").set("spark.ui.port","20202");
sc=SparkContext(conf=conf)

SET spark.sql.hive.version=1.2.1

dfs -ls /apps/hive/warehouse


create table orders(
order_id int,
order_date string,
order_customer_id int,
order_status string
) row format delimited fields terminated by ','
stored as textfile

load data local inpath '/data/retail_db/orders' into table orders;


dfs -ls /apps/hive/warehouse/iwinnerdb.db/orders

create table order_items (
  order_item_id int,
  order_item_order_id int,
  order_item_product_id int,
  order_item_quantity int,
  order_item_subtotal float,
  order_item_product_price float
) row format delimited fields terminated by ','
stored as textfile



load data local inpath '/data/retail_db/order_items' into table order_items;


orc_DB

drop table orders;
create table orders(
order_id int,
order_date string,
order_customer_id int,
order_status string
) row format delimited fields terminated by ','
stored as textfile

load data local inpath '/data/retail_db/orders' into table orders;


dfs -ls /apps/hive/warehouse/iwinnerdb.db/orders

drop table order_items
create table order_items (
  order_item_id int,
  order_item_order_id int,
  order_item_product_id int,
  order_item_quantity int,
  order_item_subtotal float,
  order_item_product_price float
) row format delimited fields terminated by ','
stored as textfile



create database dgadiraju_retail_db_orc;

create table orders_orc (
  order_id int,
  order_date string,
  order_customer_id int,
  order_status string
) stored as orc;

insert into table orders_orc select * from iwinnerdb.orders;

create table order_items_orc (
  order_item_id int,
  order_item_order_id int,
  order_item_product_id int,
  order_item_quantity int,
  order_item_subtotal float,
  order_item_product_price float
) stored as orc;

insert into table order_items_orc select * from iwinnerdb.order_items;

sqlContext.sql("use iwinnerdb")

$ sqlContext.sql("use iwinnerdb")
$ for i in sqlContext.sql("describe formatted orders").collect():print(i)

$ sqlContext.sql("select * from orders limit 10").show()

 show functions;

  describe function length
  describe function year

   select order_status, length(order_status) from orders limit 10;


   // Get COMPLETED OR CLOSED ORDER PLACED IN 2014
   select * from orders where order

   substr or substring
   instr
   like
   rlike
   length
   lcase or lower
   ucase or upper
   cast
   trim,ltrim or rtrim
   lpad ,rpad
   initcap( Default start with Cap )


substr
 select substr('Hello World,How are you',13); //How are you
 select substr('Hello World,How are you',6,8);//World,H
 select instr('rahul','ul')


 select "Hello World ,How are you" like 'World%'
 select "Hello World ,How are you" like 'World%'
 select "Hello World ,How are you" like 'World%'
 select lpad(2,12,'0');
 000000000002
 
select rpad(2,12,'0');
200000000000
 
select substr(order_date,6,2) from orders limit 10;
07
07


select cast(substr(order_date,6,2) as int) from orders limit 10;
7
7

select cast("hello" as int)
NULL

select split("Hello world,How are you",' ')
["Hello","world,How","are","you"]
select index(split("Hello world,How are you",' '),4)


current_date
current_timestamp
day
to_date
date_format(current_date)
'y'===>Year
'd'===>day
'D'===>Day number
to_unix_timestamp
date_add



select current_date
select cureent_timestamp

select current_date,date_format(current_date,'y'),date_format(current_date,'d'),date_format(current_date,'D');
OK
2018-04-07      2018    7       97


select day(current_date)

select to_date(current_timestamp)
select to_unix_timestamp(current_date)
1523073600
select from_unixtime(1523073600)

select to_date(from_unixtime(1523073600))
select to_date(order_date) from orders limit 10;

select date_add(order_date,10) from orders limit 10;


count(1)
sum(order_item_subtotal)


 select distinct order_status from orders ;

case
nvl

case   ---> if(condition) 'x' else if()

select case order_status
                 when 'CLOSED' then 'No Action'
                 when 'COMPLETE' then 'No Action_cOMPLETED'
                 when 'PENDING' then 'PENDING Action'
                 when 'PENDING' then 'PENDING Action'
                 else 'RISKY'
       end from orders limit 10


select order_status,
       case      when  order_status IN('CLOSED','COMPLETE') then 'Action CLOSED AND COMP'
                 when order_status IN('PENDING') then 'PENDING Action'
                 else 'RISKY'
       end from orders limit 10


select contact(substr(order_date,1,4),substr(order_date,6,2)) from orders limit 10
select date_format('2013-07-25 00:00:00','YYYYMM')



select o.*,c.* from orders o,customers c 
where o.order_customer_id=c.customer_id limit 100


select o.*,c.* from orders o join customers c ON  
o.order_customer_id=c.customer_id limit 100



select o.*,c.* from orders o inner join customers c ON  
o.order_customer_id=c.customer_id limit 100

select o.*,c.* from orders o left outer join customers c ON  
o.order_customer_id=c.customer_id limit 100


select count(1) from orders o inner join customers c ON  
o.order_customer_id=c.customer_id limit 100
--68883

select count(1) from customers c left outer join orders o ON  
o.order_customer_id=c.customer_id limit 100
--68913



All customers but not in orders

select * from customers c left outer join orders o ON  
o.order_customer_id=c.customer_id where o.order_customer_id is null
--30


select order_status,count(1) from order group by order_status;


select o.order_id,o.order_status,sum(oi.order_item_subtotal) order_revenue
from orders o join order_items oi
on o.order_id=oi.order_item_order_id
group by o.order_id,o.order_status



select o.order_id,o.order_status,sum(oi.order_item_subtotal) order_revenue
from orders o join order_items oi
on o.order_id=oi.order_item_order_id
group by o.order_id,o.order_status
having sum(oi.order_item_subtotal)>=100
//Dont take here order_revenue=100 because derived class fields can't access in where class\





//// Order by always sort the date by Globally

select o.order_id,o.order_date,o.order_status,sum(oi.order_item_subtotal) order_revenue
from orders o join order_items oi
on o.order_id=oi.order_item_order_id
where o.order_status in('COMPLETE','CLOSED')
group by o.order_id,o.order_status,o.order_date
having sum(oi.order_item_subtotal)>=100
order by o.order_date,order_revenue desc;


//With in that field only sort the data.
select o.order_id,o.order_date,o.order_status,sum(oi.order_item_subtotal) order_revenue
from orders o join order_items oi
on o.order_id=oi.order_item_order_id
where o.order_status in('COMPLETE','CLOSED')
group by o.order_id,o.order_status,o.order_date
having sum(oi.order_item_subtotal)>=100
distribute by o.order_date sort by o.order_date,order_revenue desc;























select o.*,c.* from orders o,customers c where
 o.order_customer_id=c.custoner_id

select o.*,c.* from orders o inner join customers c where
 o.order_customer_id=c.custoner_id

outer join

select o.*,c.* from orders o left outer join customers c where
 o.order_customer_id=c.custoner_id

select count(*) from orders o inner join customers c where
 o.order_customer_id=c.custoner_id

outer join

select count(*) from orders o left outer join customers c where
 o.order_customer_id=c.custoner_id

select * count(*) from orders o left outer join customers c where
 o.order_customer_id=c.custoner_id where 
where o.order_customer_id is null

select * from customers where customer_id not in(select)

select * from orders limit 10;

sqlContext.sql("select * from iwinnerdb.orders limit 10").show();

sqlContext.sql("select * from iwinnerdb.orders limit 10").printSchema();




sqlContext.sql("select * from iwinnerdb.orders limit 10").show();


from pyspark.sql import Row
ordersRDD=sc.textFile("/public/retail_db/orders")
type(ordersRDD)
type(ordersRDD.first)
ordersDF=ordersRDD.map(lambda o:Row(int(o.split(",")[0]),o.split(",")[1],o.split(",")[2],o.split(",")[3])).toDF();


ordersDF=ordersRDD.map(lambda o:Row(order_id=int(o.split(",")[0]),order_date=o.split(",")[1],order_customer_id=int(o.split(",")[2]),order_status=o.split(",")[3])).toDF()
ordersDF.registerTemTable("orderDF_table")
sqlContext.sql("selec * from orderDF_table").show();
sqlContext.sql("selec order_status,count(1)) from orderDF_table").show();
sqlContext.sql("selec order_status,count(1)) from orderDF_tablegroup by order_status").show();

productRaw=open("/data/retail_db/products/part-00000").read().splitlines()
type(productRaw)
productsRDD=sc.parallelize(productRaw)
for i in productsRDD.take(10):
     print(i)

productDF=productsRDD.map(lambda p: Row(product_id=int(p.split(",")[0]),product_name=p.split(",")[2])).toDF()
productDF.registerTemTable("product_temp");
sqlContext.sql("use iwinnerdb")
sqlContext.sql("show tables").show();



SELECT o.order_date,p.product_name,sum(oi.order_item_subtotal) daily_revenue_per_product FROM
orders o JOIN order_items oi
ON o.order_id=oi.order_item_order_id
JOIN products p
ON p.product_id=oi.order_item_product_id
where o.order_status IN('COMPLTE','CLOSED')
GROUP BY o.order_date,p.product_name
ORDER BY o.order_date,daily_revenue_per_product desc


sqlContext.setConf("spark.sql.shuffle.partitions","2")
sqlContext.sql("SELECT o.order_date,p.product_name,sum(oi.order_item_subtotal) daily_revenue_per_product FROM  \
orders o JOIN order_items oi \
ON o.order_id=oi.order_item_order_id \
JOIN products p \
ON p.product_id=oi.order_item_product_id \
where o.order_status IN('COMPLTE','CLOSED')\
GROUP BY o.order_date,p.product_name \
ORDER BY o.order_date,daily_revenue_per_product desc \
").show()


sqlContext.sql("create database iwinner_hdpdb")
sqlContext.sql("create table iwinner_hdpdb.daily_revenue(order_date string,product_name string,daily_revenue_per_product float) STORED AS orc")
sqlContext.sql(" insert into iwinner_hdpdb.daily_revenue_new SELECT o.order_date,p.product_name,sum(oi.order_item_subtotal) daily_revenue_per_product FROM  \
orders o JOIN order_items oi \
ON o.order_id=oi.order_item_order_id \
JOIN products p \
ON p.product_id=oi.order_item_product_id \
where o.order_status IN('COMPLTE','CLOSED')\
GROUP BY o.order_date,p.product_name \
ORDER BY o.order_date,daily_revenue_per_product desc \
")

  (OR)
daily_revenue=sqlContext.sql("SELECT o.order_date,p.product_name,sum(oi.order_item_subtotal) daily_revenue_per_product FROM  \
orders o JOIN order_items oi \
ON o.order_id=oi.order_item_order_id \
JOIN products p \
ON p.product_id=oi.order_item_product_id \
where o.order_status IN('COMPLTE','CLOSED')\
GROUP BY o.order_date,p.product_name \
ORDER BY o.order_date,daily_revenue_per_product desc")

daily_revenue.insertInto("iwinner_hdpdb.daily_revenue");
daily_revenue.printSchema()
daily_revenue.schema()
daily_revenue.show(100)
daily_revenue.save("/user/anjaiahspr/daily_revenue_save/","json")
daily_revenue.write.json("/user/anjaiahspr/daily_revenue_write/")



CREATE TABLE customers (
customer_id       int,
customer_fname    string,
customer_lname    string,
customer_email    string,
customer_password string,
customer_street   string,
customer_city     string,
customer_state    string,
customer_zipcode  string 
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

load data local inpath '/data/retail_db/customers' into table customers;

CREATE TABLE products (
product_id int, 
product_category_id int,
product_name string,
product_description string,
product_price float,
product_image string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

load data local inpath '/data/retail_db/products' into table products;