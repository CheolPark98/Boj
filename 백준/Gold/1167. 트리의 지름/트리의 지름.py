import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())

tree = [[] for i in range(n + 2)]
for i in range(1, n + 1):
    tree[n + 1].append([i, 0])
for i in range(n):
    arr = list(map(int, input().split()))
    s = arr[0]
    j = 1
    while arr[j] != -1:
        w = arr[j + 1]
        tree[s].append([arr[j], w])
        j += 2


def dfs(s):
    for edge in tree[s]:
        e, w = edge
        if dp[e] == -1:
            dp[e] = dp[s] + w
            dfs(e)


dp = [-1] * (n + 2)
dp[n + 1] = 0

dfs(n + 1)
s = dp.index(max(dp))

dp=[-1]*(n+1)
dp[s]=0
dfs(s)
print(max(dp))
