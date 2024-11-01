import json
from pathlib import Path


# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 1, "title": "Kindergarten Cop", "year": 1993}
# ] #defining the array of dictionaries

#data = json.dumps(movies)
#print(data)
#Path("movies.json").write_text(data)
#creating the json file movies.json

data = Path("movies.json").read_text() #opening the movies.json file that was created above
movies = json.loads(data) #parsing the data to return an array of dict
print(movies[1]) #accessing the entire array
print(movies[1]["title"]) #pulling just one value from array

#JSON = JavaScript Object Notation
#JSON is a popular was to format data in a was readable by humans