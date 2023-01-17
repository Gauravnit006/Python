# Functions And Docstrings

# a = 21
# b = 14
# c = sum((a, b))  # built in function

# def function1(a, b):
#     print("Hello you are in function 1", a+b)
# function1(2, 9)
# print(function1(2, 9))

def function2(a, b):
    """This is a function which will calculate the average of two number"""
    average = (a+b)/2
    print("Average of",a,"and",b,"is",average)
    return average
# function2(4, 2)
# print(function2(4, 2))
# v=function2(4, 2)
# print(v)
print(function2.__doc__)
