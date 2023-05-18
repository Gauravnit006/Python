# F-Strings & String Formatting In Python

import math

m = "laptop"
a1 = 5
a2 = 'a'
# a = "This is %s %s"%(m, a1)
# a = "This is {2} {1} {0}"
# b = a.format(m, a1, a2)
# print(b)

a = f"This is {a2} {m} {a1} {math.sin(60)}"
print(a)