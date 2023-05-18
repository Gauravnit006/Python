# Anonymous/Lambda Functions In Python

# def minus(x, y):
#     return x - y

# minus = lambda x, y:x-y
# print(minus(8, 3))

# def a_first(a):
#     return a[1]

# a_first = lambda a : a[1]

a = [[2,3], [9,1], [5,43]]
# a.sort(key = a_first)
a.sort(key=lambda x: x[1])
print(a)