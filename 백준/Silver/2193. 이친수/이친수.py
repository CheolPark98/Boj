from collections import deque
import sys

n = int(input())

dp = [[0, 0]] * 91
dp[1] = [0, 1]
dp[2] = [1, 0]

for i in range(3, 91):
    dp[i] = [dp[i - 1][1] + dp[i - 1][0], dp[i - 1][0]]

print(sum(dp[n]))