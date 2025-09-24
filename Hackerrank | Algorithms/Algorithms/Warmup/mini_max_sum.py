def miniMaxSum(arr):
    results = []
    for i in range(len(arr)):
        results.append(sum(i for i in arr) - arr[i])

    return f"{min(results)} {max(results)}"


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split(" ")))
    print(miniMaxSum(arr))