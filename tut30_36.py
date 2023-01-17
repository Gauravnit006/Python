# Pattern Printing

# Input = Integer n
# Boolean = True or False
#
# True n = 4
# *
# * *
# * * *
# * * * *
#
# False n=4
# * * * *
# * * *
# * *
# *

n = int(input("Enter the vlaue of n : "))
c = int(input("Enter the boolean value (0/1) : "))
a = bool(c)
x = n
while(n>0):
    p = n
    if a == True:
        while(p<=x):
            print("*", end=" ")
            p = p+1
        n = n-1
    else:
        i = n
        while(i>0):
            print("*",end=" ")
            i = i-1
        n = n-1
    print(end="\n")