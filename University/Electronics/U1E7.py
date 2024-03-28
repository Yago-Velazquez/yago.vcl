import csv
import sys

with open("address.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if sys.argv[1] == row["UserId"]:
            print(row["City"])