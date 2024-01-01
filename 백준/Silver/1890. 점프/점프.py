from collections import deque
import sys
from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(n)] for j in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] > 0:
            if i == n - 1 and j == n - 1:
                break
            if i + arr[i][j] < n:
                dp[i + arr[i][j]][j] += dp[i][j]
            if j + arr[i][j] < n:
                dp[i][j + arr[i][j]] += dp[i][j]
print(dp[n - 1][n - 1])

