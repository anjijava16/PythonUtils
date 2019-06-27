str = input("Enter your input: ");
print("Received input is : ", str)
file = open("F:/Works/pandas/py_master/pandas/1_intro/nyc_weather.csv")
results = []
id = 0;
for ik in file:
    id += 1
    words = ik.split(",")
    if id != 1:
        results.append((words[0], words[1], words[2], words[3], words[4]))
    else:
        print("First Value is   ", words[0], words[1], words[2], words[3], words[4])
    # print(words[0], words[1])
print(type(results))
print(results)
print(id)
for idList in results:
    # print(idList)
    print(idList[0], " ", idList[1])
    # words = line.split(',')
#         results.append((words[0], words[1:]))

# print(file)
# # File Read Operation
# r = file.read()
#
# for p in r.split(","):
#     print(p[0],"  ",p[1])
# strOne= r.split(",")
# print(strOne)
# print(r)

try:
    x = "10"
    y=20
    if x/y==0:
        print(x)
    print(int(x));
except Exception:
    print("Error")


# #File Read Of 5 Elements
# print("=======================================")
# for y in file.read():
#     print("test")
#     ps=y.split(",")
#     print(ps.index("0"))
# print("=======================================")
# print(file.read(10))
# z=r.split(",")
# print(z[0]," ",z[1])
#
# ps=file.readline();
# for res in ps:
#     print(res)
