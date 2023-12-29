N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
v = [0] * N


def dfs(n, lst):
    if n == M:
        result.append(lst)
        return
    prev = 0
    for i in range(N):
        if prev != arr[i]:
            prev = arr[i]
            dfs(n + 1, lst + [arr[i]])


dfs(0, [])
for i in result:
    print(*i)
