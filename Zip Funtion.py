list1 = [1,2,3]
list2 = [10,20,30]

zipped = list(zip(list1, list2))

print(zipped)

zipped = list(zip("abc", list1, list2)) #can also pass strings into new zipped list

print(zipped) 