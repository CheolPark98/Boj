import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b, idx):
    q = deque()
    q.append((a, b))
    sm = arr[a][b]
    v[a][b] = idx
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    v[nx][ny] = idx
                    q.append((nx, ny))
                    sm += arr[nx][ny]
                    cnt += 1
    return (sm, cnt)


cnt = 0
while 1:
    v = [[0 for i in range(n)] for _ in range(n)]
    g = []
    idx = 1
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                res = bfs(i, j, idx)
                idx += 1
                g.append(res)
    ans = []
    for i in range(len(g)):
        ans.append(g[i][0] // g[i][1])

    for i in range(n):
        for j in range(n):
            arr[i][j] = ans[v[i][j] - 1]

    cnt += 1

    if len(ans) == n * n:
        break

print(cnt-1)
