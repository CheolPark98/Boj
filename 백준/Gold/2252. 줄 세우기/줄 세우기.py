import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

g = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)

# print(g)

topo = [0] * (N + 1)
v = [0] * (N + 1)
cnt = N


def dfs(x):
    global cnt
    for e in g[x]:
        if v[e] == 0:
            v[e] = 1
            dfs(e)

            topo[e] = cnt
            cnt -= 1


for i in range(1, N + 1):
    dfs(i)

res = []

for i in range(1, N + 1):
    res.append((topo[i], i))

res.sort()
ans = []
for i in range(N):
    a, b = res[i]
    ans.append(b)

print(*ans)
