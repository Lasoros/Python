import random
import string

print(random.random()) #prints a random number between 0 and 1
print(random.randint(10 , 500)) #between two given values
print(random.choice([1, 10 , 500, 1500]))#chooses one of a select array
print(random.choices([1, 10 , 500, 1500], k=2))#chooses k amount of values from array


print(random.choices("abcdefghijklmno", k=4))
print("".join(random.choices("abcdefghijklmno", k=4))) #after selection puts them all as a string. This would be a random pass generator

print(string.ascii_letters) #prints all letters upper and lower case
print(string.ascii_lowercase) #prints lowercase
print(string.ascii_uppercase) #prints uppercase
print(string.digits) #prints 0-9 digits

print("".join(random.choices(string.ascii_letters + string.digits, k=4))) #password generator that also used numbers

numbers = [1,2,3,4]
random.shuffle(numbers) #shuffle selectino of values randomly
print(numbers)