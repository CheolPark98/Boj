import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

c, n = map(int, input().split())

h=[list(map(int,input().split())) for _ in range(n)]

dp=[1e7 for i in range(c+100)]
dp[0]=0

for cost,people in h:
    for i in range(people,c+100):
        dp[i]=min(dp[i-people]+cost,dp[i])
print(min(dp[c:]))