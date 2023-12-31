from collections import deque
import sys
from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append((0, 0, arr[0][0]))
    v = [[set() for i in range(M)] for j in range(N)]
    v[0][0].add(arr[0][0])
    while q:
        global maxn
        x, y, s = q.popleft()
        maxn = max(maxn, len(s))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            for i in range(4):
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] not in s and s + arr[nx][ny] not in v[nx][ny]:
                        v[nx][ny].add(s + arr[nx][ny])
                        q.append((nx, ny, s + arr[nx][ny]))


maxn = 0
bfs()
print(maxn)
