from pyspark import *
from operator import add

conf = (SparkConf().setMaster("local[*]").setAppName("Poc"))

sc = SparkContext(conf=conf);

print("Welcome")
print(sc)

print(sc.version)

x = [1, 2, 3, 4];

rdd1 = sc.parallelize(x);
print(rdd1.collect())

print("==================== Start Map RDD  ======")
rdd2 = rdd1.map(lambda z: (z, 1))
print(rdd2.collect())

print("========= Filter RDD ===========")
filterInfo = rdd1.filter(lambda y: y % 2 != 0)
print("Filter info ==>", filterInfo, "  ", filterInfo.collect())

print(" flatMap RDD")

str = ["hi this is anji", "how are u man", "i am doing good", "hi this is anji", "how are u man", "i am doing good"]
strdd = sc.parallelize(str);
''' flatrdd=strdd.flatMap(lambda y:y.split(' ')).map(lambda word:(word,1)).reduceByKey(lambda kj,yj:(kj,yj)) '''
flatrdd = strdd.flatMap(lambda y: y.split(' ')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
print(flatrdd.collect())

print("<<========== Groupby operation =====>")

p = ["John", "Fred", "Anna", "James", "Anoty"]

grdd = sc.parallelize(p);

gs = grdd.groupBy(lambda lg: lg[0])

for (k, v) in gs.collect():
    print("Key Value ===>", k, " List Of values ", list(v))

print("<< ========================= GroupByKeyInfo Here =========================>>")
gkey = [('B', 2), ('D', 2), ('D', 2), ('B', 4), ('C', 6), ('D', 8), ('H', 20)]
rd = sc.parallelize(gkey)


for i in rd.groupByKey().collect():
    print(i[0],list(i[1]));