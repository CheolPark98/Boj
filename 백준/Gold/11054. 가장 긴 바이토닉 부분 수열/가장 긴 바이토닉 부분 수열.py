import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[1, 1] for i in range(n)]
ans = 1
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            dp[j][0] = max(dp[j][0], dp[i][0] + 1)
            ans = max(ans, dp[j][0])
        elif arr[i] > arr[j]:
            dp[j][1] = max(dp[j][1], dp[i][0] + 1, dp[i][1] + 1)
            ans = max(ans, dp[j][1])


print(ans)
