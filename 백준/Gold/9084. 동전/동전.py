import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline


for t in range(int(input())):
    n = int(input())

    coins = [0] + list((map(int, input().split())))
    m = int(input())
    dp = [[1] + [0 for _ in range(m)] for _ in range(n + 1)]

    for i in range(1, n + 1):

        for j in range(1, m + 1):

            dp[i][j] = dp[i - 1][j]
            if j - coins[i] >= 0:
                dp[i][j] += dp[i][j - coins[i]]

    print(dp[n][m])
