print("answer = x >= y")

print("Please enter the value you wish to evaluate bool, in the form of 'answer <>= y' . . .")
x = input("x = ")
y = input("y = ")

print(f"x = {x} , y = {y}")

if x >= y:
    print("X is Greater than or Equal to Y: True")
elif x <= y:
    print("X is not Greater than or Equal to Y: False")
print(bool)