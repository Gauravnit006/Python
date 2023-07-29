# Dictionary & Its Functions in python


# d1 = {}
# print(type(d1))

d2 = {"Bottle":'Plastic', 'Apple' : 'Fruit', "Laptop" : 'Machine',
      "Ojas" : {"B" : "Roti", "L" : "Rice", "D" : "Fruit"},
      "Aarav" : [98, 92, 100]}
# print(type(d2))
# d2["Ojas"] = "Football"  # Remove previous one
# d2[123] = "Room No"
# d2["Ayush"] = [170, 150, 340]
# print(d2["Ojas"]["B"])
# print(d2["Aarav"][2])
# del d2["Ojas"]
# print((d2))

# d3 = d2  # d3 and d2 are same
# d3 = d2.copy()  # d3 is copy of d2 not same

# print(d2.get("Aarav")[2])
d2.update({100 : "Emergency"})
# print(d2)
print(d2.keys())
print(d2.items())
print(d2.values())