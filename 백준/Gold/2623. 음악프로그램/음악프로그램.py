import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for i in range(m):
    arr = list(map(int, input().split()))
    for j in range(1, arr[0]):
        g[arr[j]].append(arr[j + 1])
topo = [0] * (n + 1)
v = [0] * (n + 1)
cnt = n
flag = 0


def dfs(idx):
    global cnt, flag

    for e in g[idx]:
        if v[e] == 0:
            v[e] = 1
            dfs(e)
            topo[e] = cnt
            cnt -= 1
        elif topo[e] == 0:
            flag = 1
            return


for i in range(1, n + 1):
    dfs(i)

if flag == 1:
    print(0)
else:
    result = []

    for i in range(1, n + 1):
        result.append((topo[i], i))
    result.sort()
    for i in range(n):
        a, b = result[i]
        print(b)
