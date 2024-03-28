import random

def main():
    generate_integer(get_level())

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    score = 0
    for _ in range(10):
        X, Y = random.randint(0, pow(10, level)), random.randint(0, pow(10, level))
        eq = X + Y
        tries = 3
        while tries > 0:
            result = int(input(f"{X} + {Y} = "))
            if result != eq:
                tries -= 1
                print("EEE" if tries > 0 else eq)
            else:
                score += 1
                break
    print(f"Score: {score}")

if __name__ == "__main__":
    main()