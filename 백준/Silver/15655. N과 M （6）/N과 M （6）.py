N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
v = [0] * N


def dfs(n, lst, b):
    if n == M:
        result.append(lst)
        return
    for i in range(N):
        if v[i] == 0 and b < arr[i]:
            v[i] = 1
            dfs(n + 1, lst + [arr[i]], arr[i])
            v[i] = 0


dfs(0, [], 0)
for i in result:
    print(*i)
