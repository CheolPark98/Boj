import sys
from collections import deque
import heapq
import copy

input=sys.stdin.readline

n=int(input())

arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))
arr.sort()
dp=[0]*(n+1)
dp[0]=1

for i in range(1,n):
    mx=0
    for j in range(i):
        if arr[j][1]<arr[i][1] and dp[j]>mx:
            #print(arr[j],arr[i],dp)
            mx=dp[j]
    dp[i]=mx+1
  

print(n-max(dp))
