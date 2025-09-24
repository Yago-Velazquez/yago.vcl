# https://pypi.org/project/requests/
# https://docs.python.org/3/library/json.html
import requests
import json
import sys
def main():
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many arguments")
    else:
        try:
            print(f"{amount(convert(bitcoin()), float(sys.argv[1])):,.3f}$")
        except ValueError:
            print("Command-line argument is not a number")

def bitcoin():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    object = response.json()
    return object["bpi"]["USD"]["rate"]

def convert(string):
    return float(string.replace(",", ""))

def amount(n,m):
    return n * m



if __name__ == "__main__":
    main()
