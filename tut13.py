# Sets In Python

s = set()
# print(type(s))

# s_from_list = set([84, 219, 92])
# print(s_from_list)

s.add(1)
s.add(1)
s.add(9)
s.add(2)
s1 = {5, 3}
# s1 = s.union((1, 4, 2, 43, 5))
# s1 = s.intersection((1, 4, 2, 43, 5))
# s.remove((2))
# print(s)
# print(s, s1)
# print(len(s))
# print(min(s))
print(s.isdisjoint(s1))