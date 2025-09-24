def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    if sum(i for i in bill) / 2 == b:
        print("Bon Appetit")
    else:
        print(int(b - (sum(i for i in bill) / 2)))
if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)