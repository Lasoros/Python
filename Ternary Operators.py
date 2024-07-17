age = 22
if age >= 18 :
    #print("Eligable")
    message = "Eligible"
else:
    #print("Not Eligable")
    message = "Not Eligible"

message = "Eligible" if age >= 18 else "Not Eligible" #this is equal to the above lines of code, makes it easier and prettier
print(message)