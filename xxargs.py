def save_user(**user): #when using double asterics ** you can pass multiple keyvalue/keyword pairs to an argument Python will pacakge them into dictionary
    print(user["id"])


save_user(id = 1, name = "Tom", age = 22 )