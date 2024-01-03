from collections import deque
import sys


def solve():
    for year in range(1, 90000):
        sub_arr = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    continue
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if arr[ni][nj] == 0:
                        sub_arr[i][j] += 1
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if sub_arr[i][j] > 0:
                    arr[i][j] = max(arr[i][j] - sub_arr[i][j], 0)

        v = [[0 for _ in range(M)] for _ in range(N)]
        cnt = 0
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr[i][j] > 0 and v[i][j] == 0:
                    bfs(i, j, v)
                    cnt += 1
                    if cnt == 2:
                        return year
        if cnt == 0:
            return 0


def bfs(x, y, v):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if v[nx][ny] == 0 and arr[nx][ny] > 0:
                v[nx][ny] = 1
                q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


print(solve())
