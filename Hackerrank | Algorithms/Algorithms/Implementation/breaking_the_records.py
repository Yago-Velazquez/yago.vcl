def breakingRecords(scores):
    minimum = 0
    maximum = 0
    for i in range(1, len(scores)):
        if all(j < scores[i] for j in scores[:i]):
            maximum += 1
        elif all(j > scores[i] for j in scores[:i]):
            minimum += 1
    return f"{maximum} {minimum}"

if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)