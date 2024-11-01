items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 13),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item) #not calling the fucntion, simply passing the referance
print(items)

#a lambda fucntion is a simple anonymous function. Prevents the need to define a function

#items.sort(key= lambda parameters:expression)
items.sort(key= lambda item:item[1]) #cleaner nicer way of doing the above code
print(items)