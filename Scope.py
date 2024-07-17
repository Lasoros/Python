message = "a"

def greet(name):
    global message
    message = "c"


def send_email(name):
    message = "b"

greet("Mosh")
print(message)

#best practice is to creat parameters and functions with local variables.
#avoid global variables when able too