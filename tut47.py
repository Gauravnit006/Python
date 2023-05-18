# If __name__==__main__ usage & necessity

# import sklearn

def printer(str):
    print("Hi, how are you")
    return f"Abhi mera {str} hai"

def add(n1, n2):
    return n1 + n2

print("The file name is", __name__)

if __name__ == '__main__':
    print(printer("lab"))
    p = add(57, 2)
    print(p)