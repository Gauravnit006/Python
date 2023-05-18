# Multilevel Inheritance

class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} no of time"

class Grandson(Son):
    dance = 5
    def isdance(self):
        return f"Jackson yeah" \
            f"Yes I dance very awesomely {self.dance} no of time"

dad = Dad()
larry = Son()
karry = Grandson()

print(karry.isdance())
print(karry.basketball)