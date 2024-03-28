def main():
    frac = get_number()
    convert(frac)

def get_number():
    while True:
        try:
            fuel = input("Fraction: ").split("/")
            return (int(fuel[0]) / int(fuel[1])) * 100
        except (ValueError, ZeroDivisionError):
            pass

def convert(m):
    if m >= 99:
        print("F")
    elif m <= 1:
        print("E")
    else:
        print(f"{round(m)}%")


main()