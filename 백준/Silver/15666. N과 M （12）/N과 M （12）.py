N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
v = [0] * N


def dfs(n, lst, b):
    if n == M:
        result.append(lst)
        return
    prev = 0
    for i in range(N):
        if prev != arr[i] and arr[i] >= b:
            prev = arr[i]
            dfs(n + 1, lst + [arr[i]], arr[i])


dfs(0, [], 0)
for i in result:
    print(*i)
