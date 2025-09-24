math = str(input("Expression: ")).split(" ")
x = float(math[0])
y = math[1]
z = float(math[2])

match y:
    case "+":
        print(round(x + z, 1))
    case "-":
        print(round(x - z, 1))
    case "*":
        print(round(x * z, 1))
    case "/":
        print(round(x / z, 1))