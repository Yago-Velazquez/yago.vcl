def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i, j in zip(a, b):
        if i > j:
            alice +=1
        elif j > i:
            bob += 1
        else:
            pass
    print(alice, bob, sep=" ")


a = list(map(int, input().rstrip().split(" ")))

b = list(map(int, input().rstrip().split(" ")))

result = compareTriplets(a, b)