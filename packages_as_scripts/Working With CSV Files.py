import csv

#writing to a file
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([2000, 20, 50])

#reading a file
with open("data.csv") as file:
    reader = csv.reader(file)
    #print(list(reader)) #calling the list function to get all data from "file" and convert to list obj
    for row in reader:
        print(row)


# CSV = Coma Seperated Value (looks like a simple spread sheet stored as a plain text file