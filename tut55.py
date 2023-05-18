# Instance & Class Variables

class Employee:
    no_of_leave = 8
    pass

rohan = Employee()
mohan = Employee()

rohan.name = "Rohan"
rohan.salary = 80254
rohan.role = "Programmer"

mohan.name = "Mohan"
mohan.salary = 90000
mohan.role = "Instructor"

print(rohan.no_of_leave)
print(rohan.__dict__)
rohan.no_of_leave = 6
# Employee.no_of_leave = 4
print(Employee.__dict__)
print(mohan.no_of_leave)
