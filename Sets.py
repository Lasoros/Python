#Sets are "basically" a collection with no duplicates
#sets are defined by curly braces {}
#sets are in a "unordered collection" cannot access them using an index (see error from line 24
numbers = [1, 2, 3, 4, 4, 4, 5, 5]

uniques = set(numbers)
second = {1, 4}

#second.add(5)
#second.remove(4)
#len(second)
#print(uniques)
#print(second)

#sets are exceptionally useful due to the myriad of mathmetical operations they support

first = set(numbers)

print(first | second) # | is used to make union
print(first & second) # returns a new set that both sets contain
print(first - second) # returns what both sets do not have in common
print(first ^ second) # returns what is in the first or second but not both. IE unique values of both sets

#print(first[0])

if 1 in first:
    print("yes")