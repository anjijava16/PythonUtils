from my_package.BaseJob import *;
class InterJob(BaseJob):
    def __init__(self):
        pass;

    def __init__(self,name):
        print("name ==>",name)


    def newProcessFirstJob(self):
        print("First Hn")

    def newJobTwo(id,name):
        print("newJob")