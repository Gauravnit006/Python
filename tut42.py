# *args and **kwargs In Python

# def function_name(a, b, c, d):
#     print(a, b, c, d)
# function_name("Aarav", "Ojas", "Ayush", 29)

def funargs(normal, *args, **kwargs):
    # print(type(args))
    # print(args[2])
    print(normal)
    for i in range(0, 5):
        print(args[i])
    for key, value in kwargs.items():
        print(f"{key} eats {value}")

lists = ["Aarav", "Ojas", "Ayush", "Manish", "Shubham"]
normal = "I am a normal Argument"
kw = {"Aarav": "Apple", "Ojas": "Orange"}
funargs(normal, *lists, **kw)