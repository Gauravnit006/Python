# Scope, Global Variables and Global Keyword

# l = 10  #Global variable
# def function1(n):
#     # l=5  # local scope
#     m = 8
#     global l
#     l = l+10
#     print(l, m)
#     print(n, "I am printed")
#
# function1("This is me")
# print(l)

x = 100

def Aarav():
    x = 23  #
    def Ojas():
        global x  # directly go outside the all function
        x = 12
        print("calling Ojas()", x)
    print("Befor calling Ojas()", x)
    Ojas()
    print("After calling Ojas()", x)

Aarav()
print(x)