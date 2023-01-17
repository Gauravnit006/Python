# Using With Block To Open Python Files

# f = open("File_1.txt")
# print(f.readlines())
# print(f.readline())
# f.close()

with open("File_1.txt", "r") as f:
    a = f.readlines()
    print(a)
    # f.write("\nThanks")
    # print(f.read())

f = open("File_1.txt")
# print(f.readlines())
print(f.readlines())
f.close()