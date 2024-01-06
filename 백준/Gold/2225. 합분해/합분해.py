from collections import deque
import sys
from itertools import combinations

n, k = map(int, input().split())
dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
for i in range(k + 1):
    dp[0][i] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        for l in range(i + 1):
            dp[i][j] += dp[i - l][j - 1]

print(dp[n][k]%1000000000)
