if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    a = list(arr)
    a.sort()
    print(a[-2])
