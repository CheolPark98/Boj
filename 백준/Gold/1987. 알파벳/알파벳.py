from collections import deque
import sys
from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

v1 = [0] * 26
v2 = [[0] * M for i in range(N)]
v1[ord(arr[0][0]) - ord("A")] = 1
v2[0][0] = 1
maxn = 0


def dfs(x, y, cnt):
    global maxn
    if cnt > maxn:
        maxn = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if v1[ord(arr[nx][ny]) - ord("A")] == 0 :
                
                v1[ord(arr[nx][ny]) - ord("A")] = 1
                dfs(nx, ny, cnt + 1)
               
                v1[ord(arr[nx][ny]) - ord("A")] = 0


dfs(0, 0, 1)
print(maxn)
