# Static Methods In Python

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

    @classmethod
    def from_das(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is a good "+string)
        return 40

# rohan = Employee("Rohan", "80372", "Programmer")
# mohan = Employee("Mohan", "90000", "Instructor")
karan = Employee.from_das("Karan-45000-Tester")
# print(karan.no_of_leave)
# print(karan.printdetails())
# print(karan.printgood("laptop"))
karan.printgood("laptop")