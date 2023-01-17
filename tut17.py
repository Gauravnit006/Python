# For Loops In Python

d = {1:3,2:1}
list1 = [['Laptop', 1], ['Mouse', 2], ['keyboard', 2]]
dict1 = dict(list1)
# print(dict1)
# for item1,item2 in list1:
#     print(item1,item2<2)
# for item1, item2 in dict1.items():
#     if item2<2:
#         print(item1, item2)

#  Print the entity from list which is integer and less than 6

items = [int, float, "Aarav", "Ojas", 5, 2, 2, 0 ,8 ,1, 9 ,7]
for item in items:
    if str(item).isnumeric() and item<6 :
        print(item)