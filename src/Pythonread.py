import os;
def myFunc():
    for my in os.walk("E:\\Orla"):
        print(type(my))
        print(my)


def get_files(search_path):
    for (dirpath, _, filenames) in os.walk(search_path):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

list_files = get_files("/s3bucket/ss-trackings/")
for filename in list_files:
    fileSplit = filename.split('/')

    print("FileSplit",fileSplit)
    newDate = fileSplit[2] + "-" + fileSplit[3] + "-" + fileSplit[4];
    print(newDate)
    if(filename.__contains__("ORL")):
        print(filename)

