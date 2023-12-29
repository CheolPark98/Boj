def dfs(n, c, v, s, lst):
    if n == N:
        if c >= 2 and v >= 1:
            result.append(lst)
        return

    for i in range(s, M):
        if (
            arr[i] == "a"
            or arr[i] == "e"
            or arr[i] == "o"
            or arr[i] == "i"
            or arr[i] == "u"
        ):
            dfs(n + 1, c, v + 1, i + 1, lst + [arr[i]])
        else:
            dfs(n + 1, c + 1, v, i + 1, lst + [arr[i]])


N, M = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
result = []
dfs(0, 0, 0, 0, [])
for i in result:
    print(*i, sep="")
