#age should be between 18 and 65

age = 55

if age >= 18 and age < 65:
    print("True")
else:
    print("False")


#these are exactly the same but the below code is easier and prettier
#below is what is called "chaining comparison operators"
if 18 <= age < 65:
    print("Eligible")