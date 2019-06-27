# num = 3
#
# # Try these two variations as well.
# # num = -5
# # num = 0
#
# if num >= 0:
#     num=100;
#     print("Positive or Zero")
# else:
#     num=200
#     print("Negative number")
#

# print(num)


def sortByPlayerGroup(fed1, fed2, fed3, fed4, fed5):
    if fed1 is "null" or fed1 is None or fed1 is "NULL":
        fed1 = "Z_NA";
    else:
        fed1 = fed1
    if fed2 is "null" or fed2 is None or fed2 is "NULL":
        fed2 = "Z_NA";
    else:
        fed2 = fed2
    if fed3 is "null" or fed3 is None or fed3 is "NULL":
        fed3 = "Z_NA";
    else:
        fed3 = fed3
    if fed4 is "null" or fed4 is None or fed4 is "NULL":
        fed4 = "Z_NA";
    else:
        fed4 = fed4
    if fed5 is "null" or fed5 is None or fed5 is "NULL":
        fed5 = "Z_NA";
    else:
        fed5 = fed5
    listValues = [str(fed1), str(fed2), str(fed3), str(fed4), str(fed5)]
    sortedList = "|".join(listValues);
    return sortedList;


print(sortByPlayerGroup("10", "8", "6", "7", "2"))
# def scoreToCategory(field1, field2, field3, field4, field5):
#     f1 = ""
#     f2 = ""
#     f3 = ""
#     f4 = ""
#     f5 = ""
# if field1 is None:
#     f1 = ""
# else:
#     f1 = field1
# return field1 + "|" + field2 + "|" + field3 + "|" + field4 + "|" + field5;
