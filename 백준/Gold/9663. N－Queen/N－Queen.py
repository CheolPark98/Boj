import sys
from collections import deque
import heapq
import copy

n=int(input())

arr=[[0]*n for i in range(n)]
v1=[0]*n
v2=[0]*(2*n+1)
v3=[0]*(2*n+1)
ans=0
def dfs(a):
    global ans
    if a==n:
        ans+=1
        return
    for i in range(n):
        if v1[i]==0 and v2[i+a]==0 and v3[a-i+n]==0:
            v1[i]=1
            v2[i+a]=1
            v3[a-i+n]=1
            dfs(a+1)
            v1[i]=0
            v2[i+a]=0
            v3[a-i+n]=0
dfs(0)
print(ans)