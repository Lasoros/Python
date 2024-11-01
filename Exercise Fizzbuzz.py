# def fizz_buzz(input):
#     remainder = 0
#     if (input % 3 == remainder) and not (input & 5 == remainder):
#         print("Fizz")
#     elif (input % 5 == remainder) and not (input % 3 == remainder):
#         print("Buzz")
#     elif (input % 3 == remainder) and (input % 5 == remainder):
#         print("FizzBuzz")
#     else:
#         print(input)

def fizz_buzz1(input):
    remainder = 0
    if (input % 3 == remainder) and (input % 5 == remainder):
        print("FizzBuzz")
        #use return for better code
    elif (input % 3 == remainder) and not (input % 5 == remainder):
        print("Fizz")
    elif (input % 5 == remainder) and not (input % 3 == remainder):
        print("Buzz")
    else:
        return input

def fizz_buzz_cleaner(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz1(12))