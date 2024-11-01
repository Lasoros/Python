letters = ["a", "b", "c", "d"]


letters[0] = "A" #access and change list item at [location]
print(letters[0:3])
print(letters[:3]) #if no first arguement is passed zero is assumed
print(letters[0:]) #if no last is passed the full length will be used
print(letters)


numbers = list(range(20))

print(numbers)
print(numbers[::2]) #iterating/stepping through list
print(numbers[::-1]) #returns all reversed