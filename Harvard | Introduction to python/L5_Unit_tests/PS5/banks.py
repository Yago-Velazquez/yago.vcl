def main():
    gr = input("Greeting: ")
    print(f"Owed: {value(gr)}$")

def value(greeting):
    greet = greeting.split(" ")
    match greet[0]:
        case "Hello" | "hello" | "Hello," | "hello,":
            return 0
        case _:
            match greeting[0]:
                case "H" | "h":
                    return 20
                case _:
                    return 100


if __name__ == "__main__":
    main()