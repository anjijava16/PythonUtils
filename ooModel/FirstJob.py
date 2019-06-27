from my_package.BaseJob import *;


class FirstJob(BaseJob):
    def __init__(self):
        print("<<===== FirstJob Here init(self) ===>>")
        pass;

    def __init__(self,name):
        print("<<===== FirstJob Here init(self,name) ===>>")
        print("name ==>",name)



    def newProcessFirstJob(self):
        print("First Hn")

    def newJobTwo(id,name):
        print("newJob")
