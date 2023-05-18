# Class Methods In Python

class Employee:
    no_of_leave = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. And the role is {self.role}."

    @classmethod
    def change_leave(cls, newleaves):
        cls.no_of_leave = newleaves

rohan = Employee("Rohan", "80372", "Programmer")
mohan = Employee("Mohan", "90000", "Instructor")
# rohan.change_leave(29)
rohan.no_of_leave = 5
print(mohan.no_of_leave)
print(rohan.__dict__)