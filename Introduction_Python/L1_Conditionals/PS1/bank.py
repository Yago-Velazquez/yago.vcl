greeting = str(input("Greeting: "))
greeting = greeting.split(" ")
g = greeting[0]
match g:
    case "Hello" | "hello" | "Hello," | "hello,":
        print("0$")
    case _:
        match g[0]:
            case "H" | "h":
                print("20$")
            case _:
                print("100$")