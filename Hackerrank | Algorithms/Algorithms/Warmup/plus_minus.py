def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zero += 1
    return pos/len(arr), neg/len(arr), zero/len(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split(" ")))
    
    for i in plusMinus(arr):
        print(f"{i:.{6}f}")