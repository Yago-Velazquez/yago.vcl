def main():
    meal = str(input("What time is it? "))
    meal = convert(meal)
    if 7 <= meal <= 8:
        print("Breakfast time")
    elif 12 <= meal <= 13:
        print("Lunch time")
    elif 18 <= meal <= 19:
        print("Dinner time")

def convert(time):
    time = float(time.replace(":", "."))
    return time

if __name__ == "__main__":
    main()