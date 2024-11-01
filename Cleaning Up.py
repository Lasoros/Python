try:

    file = open("test.txt")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a vaild age. . .")
else:
    print("No exceptions were thrown")
finally: #finally clause is always executed whether an exception is found or not
         #whenever opening a resource (test.txt) always remember to close it to free up external resources (database conn, network conn, files, etc)
    file.close()