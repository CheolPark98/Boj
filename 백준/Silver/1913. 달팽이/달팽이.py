import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input())
num = int(input())
arr = [[0 for i in range(N)] for i in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
xi, yi = 0, 0
x, y = 0, 0
v = 0
for i in range(N * N):
    arr[x][y] = N * N - i
    if N * N - i == num:
        xi, yi = x+1, y+1
    if (
        x + dx[v] >= N
        or x + dx[v] < 0
        or y + dy[v] >= N
        or y + dy[v] < 0
        or arr[x + dx[v]][y + dy[v]] != 0
    ):
        v = (v + 1) % 4
    x, y = x + dx[v], y + dy[v]

for i in arr:
    print(*i)

print(xi, yi)
