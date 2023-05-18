# Decorators In Python

# def function1():
#     print("Good morning")
#
# func2 = function1
#
# del function1
# def function1():
#     print("Good night")
# function1()
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("This is a device")
# executor(print)

def dec1(func1):
    def nowexex():
        print("Executing now")
        func1()
        print("Executed")
    return nowexex
@dec1
def who_is_he():
    print("He is Aarav")

# who_is_he = dec1(who_is_he)  # @dec1
who_is_he()