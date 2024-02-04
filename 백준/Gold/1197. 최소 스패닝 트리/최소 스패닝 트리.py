import sys
import heapq
import math

input = sys.stdin.readline


def find_p(x):
    if p[x] == x:
        return x
    p[x] = find_p(p[x])
    return p[x]


def union_p(x, y):
    a, b = find_p(x), find_p(y)
    if a > b:
        p[a] = b
    else:
        p[b] = a


n, m = map(int, input().split())

edges = []

for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))
edges.sort()
p = [i for i in range(n + 1)]
s = 0
for edge in edges:
    w, x, y = edge
    if find_p(x) != find_p(y):
        union_p(x, y)
        s += w
print(s)
