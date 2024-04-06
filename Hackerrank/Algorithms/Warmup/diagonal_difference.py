def diagonalDifference(arr):
    main_diagonal = []
    secondary_diagonal = []
    for i in range(len(arr)):
        main_diagonal.append(arr[i][i])
    for i in range(len(arr)):
        secondary_diagonal.append(arr[i][(len(arr)-i-1)])
    return abs(sum(i for i in main_diagonal)- sum(i for i in secondary_diagonal))



if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split(" "))))
    result = diagonalDifference(arr)
    print(result)