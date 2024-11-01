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

m = Mammal()

print(isinstance(m, Mammal)) #Mammal inherits from Animal
print(isinstance(m, Animal)) #Animal inherits from Object
print(isinstance(m, object)) #All things in Python are Object at there basest

print(issubclass(Mammal, object))