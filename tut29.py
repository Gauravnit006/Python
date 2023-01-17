# Writing And Appending To A File

# f = open("file_1.txt", "w")  # Remove all the content in file and then write
# f = open("file_1.txt", "a")  # Add the content with previous content
# p = f.write("\nAarav and Ojas are a good boy.")
# print(p)
# f.close()


# f = open("file_1.txt", "a")  # Add the content with previous content
# p = f.write("\nAarav and Ojas are a good boy.")
# print(p)
# f.close()

f = open("File_1.txt", "r+")
print(f.read())
f.write("Thank You\n")
f.close()