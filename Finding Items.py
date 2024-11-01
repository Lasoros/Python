letters = ["a", "b", "c"]

print(letters.index("a"))
#print(letters.index("d")) python returns an error for this. Most other languages, IE C based languages, return -1

if "d" in letters:
    print(letters.index("d")) #this will prevent errors from showing

print(letters.count("d"))