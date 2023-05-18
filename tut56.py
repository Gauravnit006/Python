# Self & __init__() (Constructors)


class Employee:
    no_of_leave = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. And the role is {self.role}."
# rohan = Employee()
# mohan = Employee()
#
# rohan.name = "Rohan"
# rohan.salary = 80254
# rohan.role = "Programmer"
#
# mohan.name = "Mohan"
# mohan.salary = 90000
# mohan.role = "Instructor"
#
# print(rohan.printdetails())

rohan = Employee("Rohan", "80372", "Programmer")
mohan = Employee("Mohan", "90000", "Instructor")
print(rohan.salary)