

class Animal:

    def __init__(self):
        self.age = 1
    def eat(self): #DRY: Dont Repeat Yourself
        print("eat")

# Animal: Parent, Base
# Mammal: Child. Sub
class Mammal(Animal):
    # def eat(self): #DRY: Dont Repeat Yourself Negated by Inheriting Mammal(Animal) <------
    #     print("eat")

    def walk(self):
        print("walk")

class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammal()

m.eat()

print(m.age)