from validator_collection import checkers


def main():
    if validation(input("EMAIL: ")): print("Valid")
    else: print("Invalid")

def validation(s):
    return checkers.is_email(s)

if __name__ == "__main__":
    main()