# class Employee:
#     def greet(self):
#         print("Empoyee Greet")
#
# class Person:
#     def greet(self):
#         print("Person Greet")
#
# class Manager(Employee, Person):
#     pass
#
# class Manager(Employee, Person):
#     pass
# manager = Manager()
# manager.greet() #looks for the first .greet method and stops. Spits out Employee
# Above is a example of bad multiple inheritance

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FLyingFish(Flyer, Swimmer):
    pass

