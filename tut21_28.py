# Python Exercise 3

'''Take the number until it is not to original number in under limited guesses'''

# no of guesses 9
# print no of guesses left
# no of guesses he took to finish
# if guesses is complete print game over

n = 9  # Number of guesses
a = 18 # Original number
print("Guess the original number")
print("Number of guesses you have : ", n)

while n > 0:
    num = int(input("\nEnter the number you want to guess : "))
    if num < a :
        print("Guessed number is less than original number")
        if n == 1 :
            print("Game over !!")
            break
        n = n - 1
        print("The number of guesses you have remains :", n)
        continue
    elif num > a :
        print("Guessed number is greater than original number")
        if n == 1 :
            print("Game over !!")
            break
        n = n - 1
        print("The number of guesses you have remains :", n)
        continue
    elif num == a :
        print("Congratulation you successfully guessed original number in", 9 - n +1, "guesses  !!")
        break
