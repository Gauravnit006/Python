# Break & Continue Statements In Python

i=0

while(True):
    if i % 2 ==0:
        i = i+1
        continue
    print(i, end=" ")
    if i == 49:
        break
    i = i+1