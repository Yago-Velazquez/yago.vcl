import re
import sys


def main():
    print("Valid") if validate(input("IP: ")) else sys.exit("Invalid")


def validate(ip):
    matches = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if matches and all(int(group) in range(256) for group in matches.groups()): return True


if __name__ == "__main__":
    main()