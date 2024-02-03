import sys
import heapq
import math

input = sys.stdin.readline

n = int(input())

g = [list(map(float, input().split())) for i in range(n)]

edges = []

for i in range(n):
    for j in range(i + 1, n):
        edges.append(
            (math.sqrt(pow(g[i][0] - g[j][0], 2) + pow(g[i][1] - g[j][1], 2)), i, j)
        )


d = [0] * n
v = [0] * n
p = [i for i in range(n)]


def find_p(x):
    if p[x] != x:
        p[x] = find_p(p[x])
    return p[x]


def union_p(x, y):
    a, b = find_p(x), find_p(y)
    if a < b:
        p[b] = a
    else:
        p[a] = b


edges.sort()
s = 0

for edge in edges:
    d, x, y = edge
    if find_p(x) != find_p(y):
        union_p(x, y)
        s += d

print(f"{s:.2f}")
