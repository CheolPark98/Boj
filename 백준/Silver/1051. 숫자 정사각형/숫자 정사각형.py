import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().rstrip())) for i in range(N)]

result = 1

for i in range(N - 1):
    for j in range(M - 1):
        r = min(M - j, N - i)
        for k in range(1, r):
            if (
                arr[i][j] == arr[i][j + k]
                and arr[i][j] == arr[i + k][j]
                and arr[i][j] == arr[i + k][j + k]
            ):

                v = (1 + k) * (1 + k)
                if v > result:
                    result = v
print(result)
