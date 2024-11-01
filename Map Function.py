items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 13),
]


# prices = []
# for item in items:
#     prices.append(item[1])
#
# print(prices)
# use code below instead, nicer to look and and more efficient

#transfrom/mapped this list into a different list

prices = list(map(lambda item: item[1], items))
print(prices)

#map function takes a lambda function and applies it to every item, item[1], of the iterable, items.