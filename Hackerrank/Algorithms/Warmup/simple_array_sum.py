def simpleArraySum(ar):
    return sum(i for i in ar)

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(simpleArraySum(ar))