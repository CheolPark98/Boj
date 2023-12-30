from collections import deque
import sys

N, M, H = map(int, input().split())

arr = [[list(map(int, input().split())) for i in range(M)] for j in range(H)]

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

def bfs():
    v = [[[0] * N for i in range(M)] for j in range(H)]
    q = deque()
    cnt = 0
    for h in range(H):
        for i in range(M):
            for j in range(N):
                if arr[h][i][j] == 1:
                    q.append((h, i, j))
                elif arr[h][i][j] == 0:
                    cnt += 1
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < H and 0 <= nx < M and 0 <= ny < N:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = 1
                    q.append((nz, nx, ny))
                    v[nz][nx][ny] = v[z][x][y] + 1
                    cnt -= 1
    max = -1
    for h in range(H):
        for i in range(M):
            for j in range(N):
                if v[h][i][j] > max:
                    max = v[h][i][j]
    if cnt > 0:
        return -1
    return max

print(bfs())
