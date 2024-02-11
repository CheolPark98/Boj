import sys
import heapq
import math
from collections import deque

input = sys.stdin.readline

n = int(input())

dp = [[0, 0] for i in range(50)]


dp[1][1] = 3
dp[1][0] = 2

for i in range(3, 49, 2):
    dp[i][0] = dp[i - 2][1] * 2 + dp[i - 2][0]
    dp[i][1] = dp[i - 2][1] * 3 + dp[i - 2][0]

print(dp[n - 1][1])
