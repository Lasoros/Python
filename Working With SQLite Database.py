import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())
# #print(movies)
#
#Below: writing to a SQLite database from file
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT OR IGNORE INTO Movies VALUES(?, ?, ?)" #just "INSERT INTO Movies "INSERT INTO Movies VALUES(?, ?, ?)" didnt work.
#     #needed to add "INSERT OR IGNORE" or "INSERT OR REPLACE" to fix.
#     #had both id values set to 1, returned error. Fixed by fixed value to be not both set to 1
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#         conn.commit() #only needed when writing data to a database

#below: reading from a SQLite file (happened to be created above)
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command) #cursor is an iterable obj
    # for row in cursor:
    #     print(row) #need to comment these out as once the end of an iterable has been reached can no longer interate as it will be at end
    movies = cursor.fetchall()
    print(movies)