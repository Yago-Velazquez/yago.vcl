def birthday(s, d, m):
    count = 0
    if len(s) == 1:
        if s[0] == d:
            count += 1
    else:
        for i in range(len(s)-m+1):
            if sum(items for items in s[i:i+m]) == d:
                count += 1
    return count

if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    d, m = map(int, input().strip().split())
    result = birthday(s, d, m)
    print(result)