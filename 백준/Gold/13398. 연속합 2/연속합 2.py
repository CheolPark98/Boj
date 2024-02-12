import sys
import heapq
import math
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
m = min(arr)
dp = [[m, m] for i in range(n)]
dp[0][0] = arr[0]
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
if n >= 2:
    for i in range(2, n):
        dp[i][1] = max(dp[i - 2][0] + arr[i], dp[i - 1][1] + arr[i])
mx = max(max(dp))
for i in range(n):
    mx = max(mx, dp[i][1])
print(mx)
