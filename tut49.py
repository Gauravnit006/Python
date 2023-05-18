# Map, Filter & Reduce

# numbers = ["5", "39", "12"]

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers = list(map(int, numbers))
# print(numbers)

# numbers[2] = numbers[2] + 2
# print(numbers[2])

# def sq(a):
#     return a*a

num = [2, 9, 29, 22, 58, 19]
# square = list(map(sq, num))
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# for i in range(len(num)):
#     a = num[i]
#     val = list(map(lambda x: x(a), func))
#     print(val)

# -----------------------Filter-----------------------------

# def is_greater_5(num):
#     return num>5
#
# lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# greater_than_5 = list(filter(is_greater_5, lists))
# print(greater_than_5)

# -----------------------Reduce-----------------------------

from functools import reduce

list1 = [1, 2, 3, 4, 9, 3]
nums = reduce(lambda x, y: x + y, list1)
print(nums)