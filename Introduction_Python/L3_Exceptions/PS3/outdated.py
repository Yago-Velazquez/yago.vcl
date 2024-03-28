def main():
    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
    while True:
        date = input("Date: ")
        if "/" in date:
            date = date.split("/")
            return print(f"{date[2]}-{date[0]}-{date[1]}")
        else:
            for month in months:
                if month in date:
                    date = date.split(" ")
                    if date[0] == month and date[2].isdigit():
                        date[1] = date[1].removesuffix(",")
                        if date[1].isdigit():
                            return print(f"{date[2]}-{months[month]}-{date[1]}")
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

main()
