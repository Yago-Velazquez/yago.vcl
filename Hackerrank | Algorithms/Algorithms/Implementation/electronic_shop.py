def getMoneySpent(keyboards, drives, b):
    t = list()
    for k in keyboards:
        for d in drives:
            if k + d <= b: t.append(k + d)
    if len(t) != 0: print(max(t))
    else: print("-1")

if __name__ == '__main__':
    b, n, m = map(int, input().rstrip().split())
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)