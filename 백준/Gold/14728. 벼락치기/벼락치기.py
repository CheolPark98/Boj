import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, t = map(int, input().split())

arr = []

for i in range(n):
    k, s = map(int, input().split())
    arr.append((k, s))

dp = [0] * (t + 1)

for i in range(n):
    for j in range(t, 0, -1):
        if j >= arr[i][0]:
            dp[j] = max(dp[j - arr[i][0]] + arr[i][1], dp[j])

print(max(dp))
