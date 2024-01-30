import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

dp = [[[0, 0, 0] for i in range(n)] for i in range(n)]

dp[0][1][0] = 1
pos = [[0, 0], [1, 2]]

for x in range(n):
    for y in range(n):
        for z in range(3):
            if z == 0:
                for dx, dy in ((0, 1), (1, 1)):
                    nx, ny = dx + x, dy + y

                    if nx < n and ny < n and arr[nx][ny] != 1:
                        if dx == 1 and dy == 1:
                            if arr[nx][y] == 1 or arr[x][ny] == 1:
                                continue
                        dp[nx][ny][pos[dx][dy]] += dp[x][y][z]

            if z == 1:
                for dx, dy in ((1, 0), (1, 1)):
                    nx, ny = dx + x, dy + y
                    if nx < n and ny < n and arr[nx][ny] != 1:
                        if dx == 1 and dy == 1:
                            if arr[nx][y] == 1 or arr[x][ny] == 1:
                                continue
                        dp[nx][ny][pos[dx][dy]] += dp[x][y][z]

            if z == 2:
                for dx, dy in ((0, 1), (1, 1), (1, 0)):
                    nx, ny = dx + x, dy + y
                    if nx < n and ny < n and arr[nx][ny] != 1:
                        if dx == 1 and dy == 1:
                            if arr[nx][y] == 1 or arr[x][ny] == 1:
                                continue
                        dp[nx][ny][pos[dx][dy]] += dp[x][y][z]


print(sum(dp[n - 1][n - 1]))
