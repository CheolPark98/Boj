from collections import deque
import sys
import heapq
from itertools import combinations
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            cnt += 1
cnt -= 3

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(carr):
    global cnt
    scnt = cnt
    q = deque()
    for i in range(n):
        for j in range(m):
            if carr[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if carr[nx][ny] == 0:
                    carr[nx][ny] = 2
                    q.append((nx, ny))
                    scnt -= 1
    global ans
    ans = max(scnt, ans)


ans = 0

x_y = [(x, y) for y in range(m) for x in range(n) if not arr[x][y]]

for c in combinations(x_y, 3):
    tmp = copy.deepcopy(arr)
    for x, y in c:
        tmp[x][y] = 1
    bfs(tmp)

print(ans)
