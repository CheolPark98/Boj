import sys
from collections import deque
import heapq
import copy

def dfs(n,lst,b):
    if (n==M):

        result.append(lst)
        return
    
    for j in range(1,N+1):
        if v[j]==0:
            v[j]=1
            a=arr[j]
            dfs(n+1,lst+[a],j)
            v[j]=0


N,M=map(int,input().split())
v=[0]*(N+1)
arr=[0]+list(map(int,input().split()))
arr.sort()

result=[]
dfs(0,[],0)

for i in result:
    print(*i)