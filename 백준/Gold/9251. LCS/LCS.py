import sys
from collections import deque
import heapq

input = sys.stdin.readline

w1 = list(map(str, input().rstrip()))
w2 = list(map(str, input().rstrip()))

l1, l2 = len(w1), len(w2)

dp = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < dp[j]:
            cnt = dp[j]
        elif w1[i] == w2[j]:
            dp[j] = cnt + 1

print(max(dp))
