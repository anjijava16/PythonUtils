# Python Libray Full Info 

# https://docs.python.org/2/library/


# Python Coding standards-best-practices

## https://www.python.org/dev/peps/pep-0008/


https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3


https://realpython.com/intermediate-python-project-ideas/#bulk-file-rename-tool


https://www.programcreek.com/python/example/56509/dateutil



# ========================================================

# Python Setup in Windows (Using Windows System)
from pyspark import *;
import os
os.environ["SPARK_HOME"] = "D:/Spark1.6/spark-1.6.3-bin-hadoop2.6"
print("Starting Before Main Method here")

if __name__ == "__main__":
    #conf = SparkConf().setAppName("MainMethod Here").setMaster("local[*]");
    #sc = SparkContext(conf=conf);
    sc = SparkContext("local", "SparkDemo");
    # Read input file
    lines = sc.textFile("C:\Users\Welcome\Dropbox\VLInfo\TAR_IPF_DSci\\word.txt");
    # Collect RDD to a list
    llist = lines.collect();

    print("Process Here ")
    # Print the List
    for line in llist:
        print(line)

JSON	Python
object	dict
array	list
string	str
number (int)	int
number (real)	float
true	True
false	False
null	None

# PythonUtils

# Python (Udemy ): https://www.udemy.com/learn-python-3-from-beginner-to-advanced/learn/v4/content

# Data analysis and Pandas :: https://www.udemy.com/data-analysis-with-pandas/learn/v4/content

