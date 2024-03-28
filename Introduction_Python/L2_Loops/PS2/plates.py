def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return all(valid_characters(s), length(s), position(s))

def valid_characters(s):
    return all(i.isalnum() for i in s)

def length(s):
    return 2 <= len(s) <= 6

def position(s):
    if "0" in s:
        pos_num = s.find("0")-1
        numero = s[pos_num]
        return numero.isdigit() and s[0:2].isalpha and s[len(s)-1].isdigit()
    elif any(i.isdigit() for i in s):
        return s[0:2].isalpha and s[len(s)-1].isdigit()
    else:
        return True

main()
