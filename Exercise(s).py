
# for number in range(0 ,10 , 2):
#     if number == 0:
#         print("")
#     elif number < 10:
#         print(number)
#     else:
#         print("We have " number+1 " even numbers")


number = 0
num = 0

counter = 0

# while number <= 10:
#     for number in range(0, 10, 2):
#         if number == 0:
#             print("")
#         elif number < 10:
#             print(number)
#     else:
#         print("We have "  " even numbers")
#     break

# while number <= 10:
#     for number in range(1, 10):
#         if number % 2 == 0:
#             counter = +1
#             print(number)
#         else number == 10:
#             print(f"We have {counter} even numbers")
#     break

for number in range(1, 10):
    if number % 2 == 0:
        counter += 1
        print(number)
print(f"We have {counter} even numbers")


