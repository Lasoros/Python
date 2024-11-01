x = 10
y = 11

if x != y:
    swap_X = x
    swap_Y = y
    x = swap_Y
    y = swap_X
    print("The original value for X =", swap_X, "The original value for Y =", swap_Y)
    print("The value for X =", x, "The value for Y = ", y)


x, y = y, x #this is a much easier way that exists in python to swap variables

a, b = 1, 2 #defining a tuple on the right side just without the () 