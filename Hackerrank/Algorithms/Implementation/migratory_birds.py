def migratoryBirds(arr):
    items = []
    s = list(arr.count(i) for i in set(arr))
    for i in list(set(arr)):
        if arr.count(i) == max(s):
            items.append(i)
    print(min(items))



if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)