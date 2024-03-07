import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(x, c):
    visited[x] = c
    c = c % 2 + 1
    for y in g[x]:
        if visited[y] == 0:
            visited[y] = c
            bfs(y, c)


for i in range(int(input())):
    flag = 0
    v, e = map(int, input().split())
    visited = [0] * (v + 1)

    g = [[] for i in range(v + 1)]

    for i in range(e):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == 0:
            bfs(i, 1)
    flag = 0

    for i in range(1, v + 1):
        for j in g[i]:
            if visited[j] == visited[i]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")
