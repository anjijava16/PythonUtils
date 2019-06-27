from my_package.FirstJob import *;
class FinalJob(FirstJob):

    def __init__(self):
        pass;

    def __init__(self,name):
        print("name ==>",name)
        pass
    def process(self):
        pass;
    def driverJobRunning(self,start_dt, end_dt, max_data_load_dt,spark, s3_bucket):
        print("start_dt==>",start_dt)
        print("end_dt==>", end_dt)
        print("max_data_load_dt==>", max_data_load_dt)
        print("spark==>", spark)
        print("s3_bucket==>", s3_bucket)




if __name__ == "__main__":
    job=FinalJob("vyge_strm_ctgy_dly");
    #job.display()
    job.newProcessFirstJob()

    job.sparkJobStartHere();
    job.baseTestProcessJob();
    job.driverJobRunning("start_dt:2018-08-08","end_dt:2018-08-08","max_data_dt:2018-09-10","sparkJob","hdfs");




