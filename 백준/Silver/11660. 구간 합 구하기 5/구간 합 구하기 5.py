from collections import deque
import sys
from itertools import combinations

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]
idx = [list(map(int, input().split())) for i in range(m)]
if n > 1:
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][0] = arr[i][0]
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + arr[i][j]

    for i in range(m):
        sum = 0
        for j in range(idx[i][0] - 1, idx[i][2]):
            sum = (
                sum
                + dp[j][idx[i][3] - 1]
                - dp[j][idx[i][1] - 1]
                + arr[j][idx[i][1] - 1]
            )

        print(sum)
else:
    for i in range(m):
        print(arr[0][0])
