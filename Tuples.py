point = (1, 2, 3, 4)
single_int = 1
single_point_tup = 1, #when using a tuple with just one number use a trailing coma so python doesn't think to define an int
pointEZ = 1, 2, 3, 4 #dont need to use () as python will see it as a tuples anyway
point_empty = () #use () when defining an empty tuple

point_concat = point + pointEZ + (5, 0) + (8, 41) #can easily concactinate tuples
point_repeat = point * 2 #repeat via multiplication

point_convert = tuple("Hello World")

print(type(single_int))
print(type(single_point_tup))
print(point_concat)
print(point_repeat)
print(point_convert)