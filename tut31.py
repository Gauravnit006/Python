# Seek(), tell() & More On Python Files

f = open("File_1.txt")
print(f.readline())
# print(f.tell())
f.seek(17)
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.tell())
f.close()