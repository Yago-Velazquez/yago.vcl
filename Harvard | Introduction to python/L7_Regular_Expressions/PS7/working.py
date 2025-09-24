import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.match(r"^(\d{1,2})\:?(\d{2})? (A|P)M to (\d{1,2})\:?(\d{2})? (A|P)M$", s)
    hour1, min1, time1, hour2, min2, time2 = match.groups()
    return f"{change_time(hour1, time1)}{minutes(min1)} to {change_time(hour2, time2)}{minutes(min2)}"


def change_time(hour, time):
    if "P" in time: return int(hour) + 12
    else: return hour

def minutes(minute):
    if minute is not None and int(minute) in range(0, 60): return f":{minute}"
    elif minute is None: return ":00"
    else: return sys.exit(f"Minute {minute} out of range")


if __name__ == "__main__":
    main()