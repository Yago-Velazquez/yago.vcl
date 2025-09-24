def main():
    x = int(input("What is the width? "))
    y = int(input("What is the height? "))
    brick(x,y)

def brick(width, height):
    for _ in range(height):
        print("#" * width)

main()