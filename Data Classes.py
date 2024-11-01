from collections import namedtuple

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#tedious to do the above can instead used a namedtuple, see below

Point = namedtuple("Point",["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

print(id(p1), id(p2)) #id prints the memory address where it is stored

print(p1 == p2)


