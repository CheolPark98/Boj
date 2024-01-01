from collections import deque
import sys
from itertools import combinations

n = int(input())
dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1] for i in range(n + 1)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    for j in range(9):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(sum(dp[n])%10007)
