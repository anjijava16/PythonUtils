from flatten_json import flatten
import sys
import json
import io
import csv
import urllib
import os
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
            input_file = open(file_full_path, "r")
            # *.json
            # split to get details
            path_splits = file_full_path.split('/')
            game_code = path_splits[7][0:10]
            year = game_code[0:4]
            month = game_code[4:6]
            day = game_code[6:8]
            file_name = "year=" + path_splits[1] + "/month=" + path_splits[2] + "/day=" + path_splits[
                3] + "/game_code=" + game_code + "/" + game_code + '.csv'

            # 2018031729.csv
            print(file_name)

            csv_out = io.BytesIO()
            csv_file = csv.writer(csv_out)  # create a csv.write

            flatten_str = ""
            header_written = False
            # each line represents spatial position in json format
            for line in input_file.read().split('\n'):
                try:
                    tmp = json.loads(line)

                    # flatten tracking data
                    flatten_str = flatten(tmp)
                    print(flatten_str)
                    print(type(flatten_str))
                    if header_written == False:
                        header_written = True
                        csv_file.writerow(flatten_str.keys())

                    csv_file.writerow(flatten_str.values())
                except ValueError:
                    print
                    "Value Error - Ignore"
            # Write to target s3 bucket
            #target_s3 = boto3.resource('s3').Object('om-dev-ss-data', "lambda_testing/test/" + file_name)

            with open("/s3bucket/S3Writes/"+file_name, 'wt') as f:

                csv.writer()
                csv.writer(f,)

            #target_s3.put(Body=csv_out.getvalue())


def lambda_handler():
    bucket_name = 'om-dev-inbound-events'

    #targetDateNeedProcess = datetime.strftime(datetime.now(), '%Y/%m/%d')
    targetDateNeedProcess = datetime.strftime(datetime.now() - timedelta(1), '%Y/%m/%d')
    print(targetDateNeedProcess)
    targetDateNeedProcess="/11"
    process_ss_file(bucket_name, targetDateNeedProcess)
    return 'Lambda Execution From Schedular Events Info'

if __name__ == '__main__':
    lambda_handler();


import io

stream_str = io.BytesIO(b"JournalDev Python: \x00\x01")
stream_str.getvalue()
newW=open("");
newW.write(stream_str)
print(stream_str.getvalue())

