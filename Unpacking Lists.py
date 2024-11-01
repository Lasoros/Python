numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#first, second, third = numbers #list unpacking
#first, second, *other = numbers #the asteriks * tells python to pack all values into a list

first, *other, last = numbers

print(first, last, other)

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]