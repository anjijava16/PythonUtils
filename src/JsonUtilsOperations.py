import json
# json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
# parsed_json = json.loads(json_string)
# print(parsed_json)
# print(parsed_json['first_name'])
#
# fp = open("E:/creds/PythonCodes/input_01.json", 'r')
# print(type(fp))
# print(type(fp.read()))
# print(json.loads(fp.read()))
#
# json_value = fp.read()
# print(json_value.strip())
# print(json.dumps(json_value).strip())
# #raw_data = json.loads(json_value)
# #print(raw_data)requests
# #new_json=json.dumps("E:/creds/PythonCodes/input_01.json")
# #print(new_json)

import requests
import urllib3

url = "https://api.twitter.com/1/statuses/user_timeline.json"
f1 = requests.get(url).json()

#print(json.loads("E:/creds/PythonCodes/input_01.json"))

file=open("E:/creds/PythonCodes/input_01.json")
#j=json.load(file);
#print(j)
#
# with open("E:/creds/PythonCodes/input_01.json") as jsonfile:
#     jsonfile = jsonfile.de("utf-8")
#     data = json.load(jsonfile)
#     print(data)

def jsonReaderExample():
    input="E:/creds/PythonCodes/input_01.json"
    record=open(input);
    filePath=record.read();
    #print(filePath)
    js_file_info=json.dumps(filePath)
    print(js_file_info.strip().strip('""'))


print(jsonReaderExample())