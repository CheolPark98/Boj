import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(input().rstrip()) for i in range(n)]
w = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "D":
            d = [i, j]
        if arr[i][j] == "S":
            s = [i, j]
        if arr[i][j] == "*":
            w.append((i, j))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = 0
v = [[0 for i in range(m)] for j in range(n)]


def bfs():
    q = deque()
    q.append((s[0], s[1]))
    while w:
        i, j = w.pop()
        q.append((i, j))
    while q:
#        print(q)
        x, y = q.popleft()
        if arr[d[0]][d[1]] == "S":
            return
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if (arr[nx][ny] == "." or arr[nx][ny] == "D") and arr[x][y] == "S":
                    arr[nx][ny] = "S"
                    v[nx][ny] = v[x][y] + 1
                    q.append((nx, ny))
                elif (arr[nx][ny] == "." or arr[nx][ny] == "S") and arr[x][y] == "*":
                    arr[nx][ny] = "*"
                    q.append((nx, ny))


bfs()

if v[d[0]][d[1]] == 0:
    print("KAKTUS")
else:
    print(v[d[0]][d[1]])
