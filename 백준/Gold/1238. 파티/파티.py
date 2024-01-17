from collections import deque
import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m, x = map(int, input().split())
arr = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b, w = map(int, input().split())
    arr[a][b] = w


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dp = [INF] * (n + 1)
    dp[s] = 0
    while q:
        w1, v1 = heapq.heappop(q)
        if dp[v1] < w1:
            continue
        for v2 in range(1, n + 1):
            d = dp[v1] + arr[v1][v2]
            if dp[v2] > d:
                dp[v2] = d
                heapq.heappush(q, (d, v2))
    return dp


dps = [[]]
ans = []
for i in range(1, n + 1):
    dps.append(dijkstra(i))

for i in range(1, n + 1):
    ans.append(dps[i][x] + dps[x][i])
print(max(ans))

