def dayOfProgrammer(year):
    if year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print(f"12.09.{year}")
        else:
            print(f"13.09.{year}")
    elif year < 1918:
        if year % 4 == 0:
            print(f"12.09.{year}")
        else:
            print(f"13.09.{year}")
    else:
        print("26.09.1918")

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)