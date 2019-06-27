import json


def schemaJsonUtils(input_schema_path):
    jsonFile = {}
    try:
        print("Input_schema_path",input_schema_path)
        record = open(input_schema_path);
        filePath = record.read();
        jsonFile = json.loads(filePath)
        return jsonFile
    except Exception as e:
        print("Input Args==>",e.args)
        print(e)
        return jsonFile;

# json_data=schemaJsonUtils();
# print(json_data.keys())
# print(json_data.values())
# print(type(schemaJsonUtils()))

