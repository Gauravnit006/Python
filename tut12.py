''' Create the dictionary and take input from user and return the meaning
of the word from tghe dictionary '''

dt = {"Set" : "It is the collection of well defined object",
      "Mutable" : "Value can be changed",
      "Immutable" : "Value can not be changed",
      "Keyboard" : "It is used for typing"}
# print("Enter the word : ")
w1 = input("Enter the word : ")
print("The meaning of", w1, "is : ", dt.get(w1))
