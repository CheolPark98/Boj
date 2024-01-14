from collections import deque
import sys
import heapq
from itertools import combinations

input = sys.stdin.readline

n = int(input())
m = int(input())

res_arr = []

arr = [[] for i in range(n + 1)]
for i in range(m):
    a, b, w = map(int, input().split())
    arr[a].append((w, b))

s, e = map(int, input().split())

INF = int(1e9)
distance = [INF] * (n + 1)
q = []
distance[s] = 0
path = [[i] for i in range(n + 1)]
heapq.heappush(q, [0, s])
while q:
    w, v = heapq.heappop(q)

    if w > distance[v]:
        continue

    for w2, v2 in arr[v]:
        d = w2 + distance[v]
        if d < distance[v2]:
            distance[v2] = d
            path[v2] = path[v] + [v2]
            heapq.heappush(q, [d, v2])

print(distance[e])
print(len(path[e]))
print(*path[e])
