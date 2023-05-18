# Multiple Inheritance


class Employee:
    no_of_leave = 8
    # var = 7
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

class Player:
    no_of_games = 4
    var = 8
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def s(self):
        return f"Name is {self.name}. And the game he play is {self.game}."

class CoolProgrammer(Employee, Player):
    language = "C++"
    # var = 9
    def printlanguage(self):
        print(self.language)

rohan = Employee("Rohan", "80372", "Programmer")
mohan = Employee("Mohan", "90000", "Instructor")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgrammer("Karan", 92742, "CoolProgrammer")
# det = karan.printdetails()
# karan.printlanguage()
# print(det)
print(karan.var)
