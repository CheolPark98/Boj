import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().rstrip())) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dp = [[0 for i in range(m)] for j in range(n)]


v = [[0 for i in range(m)] for j in range(n)]

dic = {}


def bfs(a, b, id):
    q = deque()
    q.append((a, b))
    v[a][b] = 1
    tmp = []
    tmp.append((a, b))
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    q.append((nx, ny))
                    tmp.append((nx, ny))
                    # print(x, y, nx, ny)
                    cnt += 1
    while tmp:
        x, y = tmp.pop()
        dp[x][y] = id

    dic[id] = cnt


id = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and v[i][j] == 0:
            bfs(i, j, id)
            id += 1

for i in range(n):
    for j in range(m):
        sm = 1
        tmp = set()
        if arr[i][j] == 1:
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                    tmp.add(dp[ni][nj])

            for a in tmp:
                sm += dic[a]
            print(sm % 10, end="")
        else:
            print(0, end="")
    print()
