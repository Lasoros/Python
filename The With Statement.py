try:

    with open("test.txt") as file: #with statement is used to automatically release external resources
        print("File opened")
    
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a vaild age. . .")
else:
    print("No exceptions were thrown")

