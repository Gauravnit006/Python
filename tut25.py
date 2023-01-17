# Try Except Exception Handling In Python

num1 = input("Enter num1 : ")
num2 = input("Enter num2 : ")
try:
    print("The sum of num1 & num2 is", int(num1)+int(num2))
except Exception as e:
    print(e)

print("Must print this line")