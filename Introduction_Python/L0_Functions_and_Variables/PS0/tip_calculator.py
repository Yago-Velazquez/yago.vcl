# Define main
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Transform the check to a money value
def dollars_to_float(d):
    return float(d.removeprefix("$"))

# Transform the percentaje into a decimal number
def percent_to_float(p):
    return float(p.removesuffix("%")) / 100

# Call main
main()