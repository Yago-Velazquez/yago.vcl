# https://pypi.org/project/tabulate/
from tabulate import tabulate
import sys

if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            table = []
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File not found")
    else:
        for line in lines:
            table.append(line.rstrip().split(","))
        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
else:
    sys.exit("ERROR")