from collections import deque
import sys
from itertools import combinations

n, m = map(int, input().split())

arr = [[0, 0]] + [list(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    w = arr[i][0]
    v = arr[i][1]
    for j in range(1, m + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i-1][j - w])
print(dp[n][m])
