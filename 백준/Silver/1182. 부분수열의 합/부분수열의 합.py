import sys
from collections import deque
import heapq
import copy

n,s=map(int,input().split())

arr=list(map(int,input().split()))
result=0
def dfs(sm,i,cnt):
    global result
 
    if i==n:
        if sm==s and cnt>=1:
            result+=1
        return
   
    dfs(sm+arr[i],i+1,cnt+1)
    dfs(sm,i+1,cnt)

dfs(0,0,0)
print(result) 