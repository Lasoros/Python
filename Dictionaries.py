#dictionary is a collection of key value pairs. IE phone book has a NAME --> Contact Info
#key can only be of a immutable value (string and numbers). the value can be of any type


point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

print(point["x"])

point["x"] = 10 #change value
point["z"] = 20 #adding new value

print(point)

#print(point["a"]) # error due to no key value "a" being in dict

if "a" in point:
    print(point["a"])

print(point.get("a"))
print(point.get("a", 0)) #will return None unless otherwise told to return a sepcific value in second argue

del point["x"]
print(point)

for key in point: #how to iterate thru using a for loop
    print(key, point[key])

for key, value in point.items():
    print(key, value)