# Enumerate Function

l1 = ["Tomato", "Potato", "Chocklate", "Banana"]

# i = 1
# for items in l1:
#     if i % 2 != 0:
#         print(f"By the item -> {items}")
#     i += 1

for index, item in enumerate(l1):
    if index % 2 ==0:
        print(f"The item at {index} position is {item}")