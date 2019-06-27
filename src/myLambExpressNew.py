from flatten_json import flatten
import sys
import json
import io
import csv
import urllib
import os
import errno
from datetime import datetime, timedelta;


def get_files(search_path):
    for (dirpath, _, filenames) in os.walk(search_path):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def process_ss_file(bucket_name,prefix):


    print("Input Path ",prefix)

    trackings_file_list = get_files(prefix);



    # for each file
    for key in trackings_file_list:
        file_full_path = key
        currentDate = datetime.strftime(datetime.now(), '%Y-%m-%d')
        fileSplit = file_full_path.split('/')
        mySp = str.split("/")
        #print(mySp[3], mySp[4], mySp[5])
        newDate = fileSplit[3] + "-" + fileSplit[4] + "-" + fileSplit[5];
        # Process only json file...
        # TBD: process gz files. files from 2017 and previous years seem to have gz format
        # if file_full_path.endswith('jsonl'):
        #and( currentDate.__eq__(newDate)
        if (file_full_path.endswith('jsonl')) and (file_full_path != "ORL"):
            print("After ", file_full_path)
            #source = ss_s3.Object(bucket_name, file_full_path)
            #input_file = source.get()["Body"].read()
            input_file = open(file_full_path)
            # ss-trackings/2018/01/01/LALMIN/2018010118_nba-min_TRACKING.jsonl
            # split to get details
            path_splits = file_full_path.split('/')
            game_code = path_splits[7][0:10]
            year = game_code[0:4]
            month = game_code[4:6]
            day = game_code[6:8]
            #file_name = "year=" + path_splits[4] + "/month=" + path_splits[5] + "/day=" + path_splits[
            #    6] + "/game_code=" + game_code + "/" + game_code + '.csv'
            file_name = "year="+year+"/month="+month+"/day="+day+"/game_code="+game_code + "/" + game_code + '.csv'
            # 2018031729.csv
            print(file_name)

            #csv_out = io.BytesIO()
            csv_out = io.StringIO()
            csv_file = csv.writer(csv_out)  # create a csv.write

            flatten_str = ""
            header_written = False
            # each line represents spatial position in json format
            file_name="/s3bucket/S3Writes/"+file_name
            if not os.path.exists(os.path.dirname(file_name)):
                try:
                    os.makedirs(os.path.dirname(file_name))
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            f= open(file_name, 'w+')
            for line in input_file.read().split('\n'):
                try:
                    tmp = json.loads(line)

                    # flatten tracking data
                    flatten_str = flatten(tmp)
                    print(flatten_str)
                    print(type(flatten_str))
                    if header_written == False:
                        header_written = True
                        #csv_file.writerow(flatten_str.keys())
                    csv_file.writerow(flatten_str.values())
                except ValueError:
                    print
                    "Value Error - Ignore"
            f.write(csv_out.getvalue());
             #                 bw=io.TextIOWrapper(csv_out)
             #target_s3.put(Body=csv_out.getvalue())


def lambda_handler():
    bucket_name = 'devss'

    #targetDateNeedProcess = datetime.strftime(datetime.now(), '%Y/%m/%d')
    targetDateNeedProcess = datetime.strftime(datetime.now() - timedelta(1), '%Y/%m/%d')
    print(targetDateNeedProcess)
    targetDateNeedProcess="/s3bucket/ss"
    process_ss_file(bucket_name, targetDateNeedProcess)
    return 'Lambda Execution From Schedular Events Info'

if __name__ == '__main__':
    lambda_handler();

