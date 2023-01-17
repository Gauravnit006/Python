# Exercise 5: Health Management System

# 3 Client - Rahul, Manish, Shubham
# Total 6 files (food, exercise)
# Write a function that when executed takes as input client name
# One mor function to retrieve exercise or food for any client
# seated soldier press, cable crossover - > exercise
# [time stamp] diet/exercise -> print this
# firstly ask you want to lock the data or retrieve the data

def getdate():
    import datetime
    return datetime.datetime.now()

def locks(names):
    a = int(input("Enter 1/2 (1 for diet & 2 for exercise)"))
    x = names
    if a == 1:
        if x == "Rahul":
            with open("Rahul diet", "a") as f:
                p = input("Enter the food you want to add : ")
                f.write(p)
                f.write("\n")
        elif x == "Manish":
            with open("Manish diet", "a") as f:
                p = input("Enter the food you want to add : ")
                f.write(p)
        elif x == "Shubham":
            with open("Shubham diet", "a") as f:
                p = input("Shubham the food you want to add : ")
                f.write(p)
    elif a == 2:
        if x == "Rahul":
            with open("Rahul Exercise", "a") as f:
                p = input("Enter the exercise for Rahul : ")
                f.write(p)
        elif x == "Manish":
            with open("Manish Exercise", "a") as f:
                p = input("Enter the exercise for Manish : ")
                f.write(p)
        elif x == "Shubham":
            with open("Shubham Exercise", "a") as f:
                p = input("Enter the exercise for Shubham : ")
                f.write(p)

def retrieves(names):
    b = int(input("Enter 1/2 (1 for diet & 2 for exercise)"))
    y = names
    if b == 1 :
        if y == "Rahul" :
            with open("Rahul diet") as f:
                content = f.read()
                z = getdate()
                print("[", z, " ]", content)
        elif y == "Manish":
            with open("Manish diet") as f:
                content = f.read()
                z = getdate()
                print("[", z, " ]", content)
        elif y == "Shubham":
            with open("Shubham diet") as f:
                content = f.read()
                z = getdate()
                print("[", z, " ]", content)

    elif b == 2 :
        if y == "Rahul" :
            with open("Rahul Exercise") as f:
                content = f.read()
                z = getdate()
                print("[", z, " ]", content)
        elif y == "Manish":
            with open("Manish Exercise") as f:
                content = f.read()
                z = getdate()
                print("[", z, " ]", content)
        elif y == "Shubham":
            with open("Shubham Exercise") as f:
                content = f.read()
                z = getdate()
                print("[", z, " ]", content)


u = "yes"
# names = input("Enter the name (Rahul, Shubham, Manish)")
# op = int(input("Enter 1 for lock or 2 for retrieves"))

while(u == "yes"):
    names = input("Enter the name (Rahul, Shubham, Manish) : ")
    op = int(input("Enter 1 for lock or 2 for retrieves : "))
    if op == 1 :
        if names == "Rahul" or names == "Manish" or names == "Shubham":
            locks(names)
            print("\n")
            u = input("Do you want to repeat (yes/no) : ")
        else:
            print("You enter wrong name\n")
            u = input("Do you want to repeat (yes/no) : ")

    elif op == 2 :
        if names == "Rahul" or names == "Manish" or names == "Shubham":
            retrieves(names)
            print("\n")
            u = input("Do you want to repeat (yes/no) : ")
        else:
            print("You enter wrong name\n")
            u = input("Do you want to repeat (yes/no) : ")

    else:
        print("You enter wrong operation\n")
        u = input("Do you want to repeat (yes/no) : ")