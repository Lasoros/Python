items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 13),
]

prices = list(map(lambda item: item[1], items))

#[expressions for item in items]
prices = [item[1] for item in items] #called list comprehension, Does exactly what line 7 does

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10] #exactly the same as code above, just cleaner

print(filtered)
