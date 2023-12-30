from collections import deque
import sys

n = int(input())

arr = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []


def bfs(a, b):
    q = deque()
    q.append((a, b))
    cnt = 1
    arr[a][b]=0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))
    return cnt


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
