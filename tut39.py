# Using Python External & Built In Modules

import random

# randint(a, b) -> Any random number of range a<=N<=b
random_number = random.randint(0, 6)
# print(random_number)

# random.random() -> Any random number between 0 to 1
rand = random.random() * 100
# print(rand)

lists = ["Star Plus", "DD1", "Aaj tak", "Code with harry"]
choice = random.choice(lists)
print(choice)

# Choose two module and use it's two function
