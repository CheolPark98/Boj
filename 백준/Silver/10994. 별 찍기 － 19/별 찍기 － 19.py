import sys
from collections import deque
import heapq

input = sys.stdin.readline


N = int(input())

arr = [[" " for i in range(4 * N - 3)] for i in range(4 * N - 3)]



def fill_star(n, x, y):
    if n == 1:
        arr[x][y] = "*"
        return

    l = 4 * n - 3

    for i in range(l):
        arr[x][y + i] = "*"
        arr[x + i][y] = "*"
        arr[x + l - 1][y + i] = "*"
        arr[x + i][y + l - 1] = "*"

    fill_star(n - 1, x + 2, y + 2)


fill_star(N, 0, 0)

for i in range(4 * N - 3):
    for j in range(4 * N - 3):
        print(arr[i][j], end="")
    print()
