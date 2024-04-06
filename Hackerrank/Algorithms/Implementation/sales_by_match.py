def sockMerchant(n, ar):
    pairs = 0
    left = 0
    for i in list(set(ar)):
        pairs += ar.count(i)//2
        left += ar.count(i)%2
    assert (pairs * 2) + left == n
    return pairs

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(sockMerchant(n, ar))