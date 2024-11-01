try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError): #can use multiple exceptions with ( exceptions , exceptions )
    print("You didn't enter a vaild age. . .")
else:
    print("No exceptions were thrown")

#if anything throws an except clause it ignore all others below and exit code