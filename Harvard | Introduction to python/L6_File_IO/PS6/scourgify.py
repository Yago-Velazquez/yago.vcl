import sys
import csv

students = []

if len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row['name'], "house": row['house']})

        for student in students:
            with open(sys.argv[2], "a") as file:
                writer = csv.DictWriter(file, fieldnames=["first name", "house"])
                writer.writerow({"first name": student["name"].split(", ")[0], "house": student["house"]})
    except FileNotFoundError:
        sys.exit("File Not Found")
else:
    sys.exit("ERROR")