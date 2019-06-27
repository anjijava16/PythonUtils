class BaseJob(object):

    def __init__(self):
        print("<<===== BaseJob Here init(self) ===>>")
        pass;

    def __init__(self,name):
        print("<<===== BaseJob Here init(self,name) ===>>")
        self.name=name
        print("name of job is ===>",name)


    # def __init__(self,name,address,id):
    #     self.name="Anji"
    #     self.address="HYD"
    #     self.id="100"

    def sparkJobStartHere(self):
        print("sparkJobStartHere Job is process")

    def baseTestProcessJob(self):
        print("baseTestProcessJob processs")

# if __name__ == "__main__":
#     job=FinalJob("vyge_strm_ctgy_dly");
#     job.display()
#     job.newProcessFirstJob()
#
#     job.sparkJobStartHere();
#     job.baseTestProcessJob();
#     job.driverJobRunning("start_dt:2018-08-08","end_dt:2018-08-08","max_data_dt:2018-09-10","sparkJob","hdfs");






