import sys
import heapq
import math
from collections import deque

input = sys.stdin.readline

tc = int(input())


for i in range(tc):
    n, k = map(int, input().split())
    bt = [0] + list(map(int, input().split()))
    edges = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for j in range(k):
        s, e = map(int, input().split())
        edges[s].append(e)
        indegree[e] += 1
    target = int(input())
    q = deque()
    dp = [0] * (n + 1)
    for j in range(1, n + 1):
        if indegree[j] == 0:
            q.append(j)
            dp[j] = bt[j]

    while q:
        tmp = q.popleft()

        for j in edges[tmp]:
            indegree[j] -= 1
            dp[j] = max(dp[j], dp[tmp] + bt[j])
            if indegree[j] == 0:
                q.append(j)
    print(dp[target])
