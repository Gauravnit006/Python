# Exercise 6: Game Development: Snake Water Gun

# play 10 times
# list - > s - snake, w - water, g - gun
# Computer randomly choose on option from list & you have also choose one
# option from list
# Snake drink water but killed by gun, water destroy gun


import random

c_p = 0  # computer point
y_p = 0  # your point
i = 10   # Number of times computer and you have chances

# s - snake, w - water, g - gun
lists = ["s", "w", "g"]

while i > 0:
    your_choice = input("Enter your choice (only from s/w/g) : ")
    com_choice = random.choice(lists)
    if your_choice == 's' or your_choice == 'w' or your_choice == 'g':
        if com_choice == 's':
            if your_choice == 'w':
                print("Computer gain the point")
                c_p = c_p + 1
            elif your_choice == 'g':
                print("You gain the point")
                y_p = y_p + 1
            else:
                print("No one gain the point")

        elif com_choice == 'w':

            if your_choice == 's':
                print("you gain the point")
                y_p = y_p + 1
            elif your_choice == 'g':
                print("Computer gain the point")
                c_p = c_p + 1
            else:
                print("No one gain point")

        elif com_choice == 'g':

            if your_choice == 'w':
                print("you gain the point")
                y_p = y_p + 1
            elif your_choice == 's':
                print("Computer gain the point")
                c_p = c_p + 1
            else:
                print("No one gain the point")
        i = i - 1
        print("\n")

    else:
        print("Please enter the correct option")
        print("\n")

if y_p > c_p:
    print("You won the game !!")
elif y_p < c_p:
    print("Computer won the game !!")
else:
    print("Game Draw !!")

