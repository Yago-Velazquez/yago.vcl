def countApplesAndOranges(s, t, a, b, apples, oranges):
    number_apples, number_oranges = 0, 0
    for i in apples:
        if i + a in range(s, t+1): number_apples += 1
    for i in oranges:
        if i + b in range(s, t+1): number_oranges += 1
    return print(number_apples, number_oranges, sep="\n")

if __name__ == '__main__':
    s, t = map(int, input().rstrip().split())
    a, b = map(int, input().rstrip().split())
    m, n = map(int, input().rstrip().split())
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)