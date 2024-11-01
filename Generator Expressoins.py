from sys import getsizeof

#when using/storing an imense amount of data its best to use a generator object. They are iterable and generate the value each time
#unlike lists/arrays/etc that hold them in memory


values = (x * 2 for x in range(1000)) #no matter the size of range(X) the memory stays constant
# for x in values:
#     print(x)
print("gen:", getsizeof(values))

values = [x * 2 for x in range(1000)] #VS for a list the size of the memory is MUCH larger. USE CASE
print("list:", getsizeof(values))

#when using generator(s) you are unable to get the entire amount of items due to each being made as it iterates through
#lists store the entirety in memory so can see total amount

values = (x * 2 for x in range(1000)) #no matter the size of range(X) the memory stays constant
print(len(values)) #error due to aforementioned untackable total in a generator
