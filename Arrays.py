from array import array

#search for python 3 type code. String of 1 char determins the type of object(s)
numbers = array("i", [1, 2, 3])


#Arrays are quicker and use less memory but are usually reserved for the use of data(sets) > 10,000. Usually perfomance related
#methods to alter
numbers.append(4) #add 4 to end
numbers.insert(4, 5) #insert 4 at index 5
#numbers.pop()
#numbers.remove()

#all objects in this array are type'd to "i" or single int, anyting other type of data type with result in a error

numbers[0] = 1.0