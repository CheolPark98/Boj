from collections import deque
import sys

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(h, x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if v[nx][ny] == 0 and arr[nx][ny] > h:
                    v[nx][ny] = 1
                    q.append((nx, ny))


ans = 0
for i in range(100):
    v = [[0 for _ in range(N)] for j in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if v[j][k] == 0 and arr[j][k] > i:
                bfs(i, j, k)
                cnt += 1
    ans = max(cnt, ans)
print(ans)
