from collections import deque
import sys
from itertools import combinations

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
dp=[0]*(k+1)
dp[0]=1
for coin in arr:
    for i in range(coin,k+1):
        dp[i]+=dp[i-coin]
print(dp[k])
