
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a vaild age. . .") #this allows for the handling of exceptions without full out crashing
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution Continues")