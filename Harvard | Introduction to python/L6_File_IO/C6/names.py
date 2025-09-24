with open("names.csv", "r") as file:
    for line in sorted(file):
        print(line.rstrip())