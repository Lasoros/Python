numbers = [1, 2, 3]
print(numbers)

print(*numbers) #the asterisk, *, is the unpacking operator
#can unpack any iterable with *, doesnt have to be a list


values = list(range(5))
print(values)

values = [*range(5), *"Hello"] #unpacking both a iterable range and strimg
print(values)

first = [1, 3]
second = [2]

values = [*first, "a", *second, *"Hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z":1} #to unpack dictionaries you must use two ** instead of one
#when combining things that have the same value the last instance of that value will be used: x=1 into x=10
print(combined)

#able to use the unpacking operator to access individual value in any interable