# Define main
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Transform the check to a money value
def dollars_to_float(d):
    d1 = d.removeprefix("$")
    return float(d1)

# Transform the percentaje into a decimal number
def percent_to_float(p):
    p1 = p.removesuffix("%")
    return float(p1) / 100

# Call main
main()