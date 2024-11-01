from datetime import datetime
import time

#dt = datetime.datetime(2018, 1, 1) #this looks gross and can be avoided by using from datetime import datetime
dt1 = datetime(2018, 1, 1) #this helps when needing to create multiple datetime obj
dt2 = datetime.now()

#datetime.striptime is for parsing or conveting a date time string. Useful for user input or data file reading, both of which will be strings
dt = datetime.strptime("2018/01/01", "%Y/%m/%d") #can search for python 3 strptime, no need to memorize

dt = datetime.fromtimestamp(time.time())

print(dt)

print(f"{dt.year}/{dt.month}")

print(dt.strftime("%Y/%m")) #converts datetime obj into string. Opposite of .strptime

print(dt1 > dt2)