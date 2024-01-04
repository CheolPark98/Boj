import sys
from collections import deque
import heapq
import copy

n= int(input())
arr=[0]+list(map(int,sys.stdin.readline().split()))



dp=[0]+[1]*n

for i in range(1,n+1):
    mx=0
    for j in range(0,i):
        if arr[i]>arr[j]:
            mx=max(mx,dp[j])
    dp[i]=mx+1

print(max(dp))