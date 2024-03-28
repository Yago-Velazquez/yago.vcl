to_pay = 50
change = 0

while to_pay > 0:
    print(f"Amount due: {to_pay}")
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        to_pay -= coin
    else:
        print("Coin not accepted")

if to_pay < 0:
    change -= to_pay
    print(f"Changed owed: {change}")