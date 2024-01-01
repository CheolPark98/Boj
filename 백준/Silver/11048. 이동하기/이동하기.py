from collections import deque
import sys
from itertools import combinations

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]
dp = [[0 for j in range(m)] for i in range(n)]
dp[0][0] = arr[0][0]
for i in range(1, m):
    dp[0][i] = dp[0][i - 1] + arr[0][i]
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + arr[i][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + arr[i][j]

print(dp[n - 1][m - 1])
