def dfs(n, lst, s):
    if n == 6:
        result.append(lst)
    for i in range(s, N):
        dfs(n + 1, lst + [arr2[i]], i + 1)


while 1:
    arr = []
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    result = []
    N = arr[0]
    arr2 = arr[1:]
    dfs(0, [], 0)
    for i in result:
        print(*i)
    print()
