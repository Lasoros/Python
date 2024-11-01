values = []

for x in range(5):
    values.append(x * 2)


#[expression for item in items]

values = [x * 2 for x in range(5)] #same as lines of code above


values = {x * 2 for x in range(5)}
#{1, 2, 3, 4} just a normal set
#{1: "a", 2:"b"} a set of dictionary pairs


values = {x: x * 2 for x in range(5)}
print(values)