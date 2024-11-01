class Animal:

    def __init__(self):
        print("Animal Constructor")
        self.age = 1
    def eat(self):
        print("eat")

class Mammal(Animal):

    def __init__(self):
        print("Mammal Contructor")
        self.weight = 100
        super().__init__() #super allows access to the base class (Animal)

    def walk(self):
        print("walk")

m = Mammal()

print(m.age)
print(m.weight)

#Method Overriding is the process of replacing/extending the a method defined in the base class