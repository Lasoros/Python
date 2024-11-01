letters = ["a", "b", "c"]



#ADD
letters.append("d")
letters.insert(0, "-") #inserting hyphon at index 0

#REMOVE
letters.pop() #remving the last letter d
letters.pop(0) #removing the first item at index 0
letters.remove("b") #removes first instance of b, to remove all b's would need to loop through

del letters[0:4] #can remove range of items from list

letters.clear() #remvoes everything from list
print(letters)
