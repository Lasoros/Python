def multiply(*numbers):
    total = 1
    for number in numbers:
        #total = total * number
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# [square brackets] denote lists while (parentheses) denote tuples