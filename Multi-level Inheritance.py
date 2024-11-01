class Animal:
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird): #Exampe of bad inheritance as a chicken is a bird but cannot fly
    pass #Pass does nothing other than allow Python to not throw and error due to an empty class


# Employee - Person - Living Creature - Thing
#Try to limit inheritance to 1 or 2 levels as to avoid the above. Keep things simple as much as possible