def getTotalX(a, b):
    count = 0
    for numbers in range(max(a), min(b)+1):
        if all(check%numbers == 0 for check in b) and all(numbers%i == 0 for i in a):
            count += 1
    return count


if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(total)