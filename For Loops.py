print("Send a message")

for number in range(3):
    print("attempt", number + 1, (number + 1) * ".")

for number in range(1, 4): # passing range of values as to avoid the need for a +1
    print("attempt", number, number * ".")

for number in range(1, 10, 2): #steping or counting by the last value
    print("attempt", number, number * ".")