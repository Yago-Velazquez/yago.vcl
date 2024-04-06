def pageCount(n, p):
    n_pages = []
    total = n // 2
    n_pages.append(total - (p//2))
    n_pages.append((p)//2)
    return min(n_pages)



if __name__ == '__main__':
    n = int(input().strip())
    p = int(input().strip())
    print(pageCount(n, p))