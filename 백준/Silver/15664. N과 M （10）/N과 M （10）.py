import sys
from collections import deque
import heapq
import copy


def dfs(n,lst,b):
    if n==M:
        result.append(lst)
        return
    prev=0
    for i in range(N):
        if v[i]==0 and arr[i] != prev and b<=arr[i]:
            v[i]=1
            prev=arr[i]
            dfs(n+1,lst+[arr[i]],arr[i])
            v[i]=0

N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
result=[]
v=[0]*N
dfs(0,[],0)
for i in result:
    print(*i)