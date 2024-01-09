from collections import deque
import sys
from itertools import combinations

INF = sys.maxsize
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b, w = map(int, input().split())
    if arr[a][b] > w:
        arr[a][b] = w

for i in range(1, n + 1):
    arr[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == INF:
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()
