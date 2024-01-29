import sys
from collections import deque
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

g = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

d = [-1] * (n + 1)


def dfs(node):
    for i in g[node]:
        a, b = i
        if d[a] == -1:
            d[a] = d[node] + b
            dfs(a)


d[1] = 0
dfs(1)
s = d.index(max(d))
d = [-1] * (n + 1)
d[s]=0
dfs(s)

print(max(d))
