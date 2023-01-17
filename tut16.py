# Exercise 2 - Faulty Calculator

'''Design a calculator which will correctly solve all the problems except
the following ones :
45*3 = 555, 56+9 = 77, 56/6 = 4, 22-6=14
Your program should take operator and the two number as input from user
and then return the result'''

print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply\n4. Divide")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
Choice = int(input("Enter your choice (1/2/3/4) : "))
s = [1, 2, 3, 4]

if Choice in s:
    if Choice == 1:
        print("The sum of both given number is")
        if a == 56 and b == 9:
            print(77)
        else:
            print(a + b)
    elif Choice == 2:
        print("The subtract of both given number is")
        if a == 22 and b == 6:
            print(14)
        else:
            print(a - b)
    elif Choice == 3:
        print("The multiply of both given number is")
        if a == 45 and b == 3:
            print(555)
        else:
            print(a * b)
    elif Choice == 4:
        print("The division of both given number is")
        if a == 56 and b == 6:
            print(4)
        else:
            print(a / b)
else:
    print("Please enter given operation")