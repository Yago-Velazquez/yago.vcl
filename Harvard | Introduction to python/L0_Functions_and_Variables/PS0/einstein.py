# Define main
def main():
    mass = int(input("m: "))
    print(einstein(mass))

# Define einstein
def einstein(n):
    return n * pow(300000000, 2)

# Call main
main()