from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]
cnt = 0
sub_arr = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    global cnt
    q = deque()
    q.append((0, 0))
    v = [[0] * m for i in range(n)]
    visited = [[0] * m for i in range(n)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:
                    v[nx][ny] += 1

    for i in range(n):
        for j in range(m):
            if v[i][j] >= 2:
                arr[i][j] = 0
                cnt -= 1


t = 0
while cnt:
    bfs()
    t += 1
print(t)
