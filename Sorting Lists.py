numbers = [3, 51, 2, 8, 6]

print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort()
print(numbers)

sorted(numbers) #doesnt modify the orig list instead creates a new on that will be sorted
print(numbers)

print(sorted(numbers, reverse=True))


items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 13),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item) #not calling the fucntion, simply passing the referance
print(items)
