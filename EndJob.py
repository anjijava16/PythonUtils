from my_package.InterJob import *;


class EndJob(InterJob):
    def __init__(self):
        print("=====>>>")

    def __init__(self,name):
        print("name")


if __name__ == "__main__":
    job = EndJob("ANJI");
    #job.display()
    job.newProcessFirstJob()

    job.sparkJobStartHere();
    job.baseTestProcessJob();
    # job.driverJobRunning("start_dt:2018-08-08","end_dt:2018-08-08","max_data_dt:2018-09-10","sparkJob","hdfs");
