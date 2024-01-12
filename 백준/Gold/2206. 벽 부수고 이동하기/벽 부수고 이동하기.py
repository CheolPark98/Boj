from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().strip())) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

v = [[[0] * 2 for i in range(m)] for i in range(n)]
v[0][0][0]=1

def bfs():
    q = deque()
    q.append((0, 0, 0))

    while q:
        x, y, z = q.popleft()

        if x == n - 1 and y == m - 1:
            return v[x][y][z]
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if z == 0 and arr[nx][ny] == 1:
                    # print(nx, ny, z, arr[nx][ny])
                    v[nx][ny][1] = v[x][y][0] + 1
                    q.append((nx, ny, 1))
                elif v[nx][ny][z] == 0 and arr[nx][ny] == 0:
                    v[nx][ny][z] = v[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1


print(bfs())
