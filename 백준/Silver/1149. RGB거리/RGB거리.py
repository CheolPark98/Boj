import sys
from collections import deque
import heapq
import copy

input=sys.stdin.readline

n= int(input())

arr=[[]]+[[0]+list(map(int,input().split())) for i in range(n)]

dp=[[0,0,0,0] for i in range(n+1)]

dp[1][1],dp[1][2],dp[1][3]= arr[1][1],arr[1][2],arr[1][3]

for i in range(2, n+1):
    dp[i][1]=min(dp[i-1][2],dp[i-1][3])+arr[i][1]
    dp[i][2]=min(dp[i-1][1],dp[i-1][3])+arr[i][2]
    dp[i][3]=min(dp[i-1][2],dp[i-1][1])+arr[i][3]

print(min(dp[n][1:]))


