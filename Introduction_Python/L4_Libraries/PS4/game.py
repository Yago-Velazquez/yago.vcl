import random

def main():
    shots(generate(get_number()))

def get_number():
    while True:
        try:
            question = int(input("Level: "))
        except ValueError:
            pass
        else:
            if question < 0:
                question
            else:
                return question

def generate(n):
    return random.choice(range(1, n+1))


def shots(m):
    count = 1
    while True:
        shot = int(input(f"Guess {count}: "))
        if shot < 0:
            shot
        elif shot == m:
            print("Just right!")
            break
        elif shot < m:
            count = count + 1
            print("Too small")
        else:
            count = count + 1
            print("Too large!")

if __name__ == "__main__":
    main()
