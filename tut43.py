# Time Module In Python

import time

# print(initial)
# initial = time.time()
#
# k = 0
# while k < 3:
#     print("This is a laptop")
#     k = k + 1
# print("Time taken by while loop : ", time.time()-initial)
# initial2 = time.time()
#
# for i in range(3):
#     print("This is a laptop")
#     time.sleep(2)
#
# print("Time taken by for loop : ", time.time()-initial2)


localtime = time.asctime(time.localtime(time.time()))
print(localtime)