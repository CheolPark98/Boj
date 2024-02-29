import sys
from collections import deque
import heapq
import copy

input=sys.stdin.readline

n,m,k=map(int,input().split())
c=[0]+list(map(int,input().split()))
p=[i for i in range(n+1)]

def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def union(x,y):
    a=find(x)
    b=find(y)
    if a<b:
        p[b]=a
    else:
        p[a]=b


for i in range(m):
    a,b=map(int,input().split())
    union(a,b)

f=[1]*(n+1)

for i in range(n+1):
    if p[i]!=i:
        tmp=find(i)
        c[tmp]+=c[i]
        f[tmp]+=1
dp=[0]*n

for i in range(1,n+1):
    if i != p[i]:
        continue
    for j in range(k-1,f[i]-1,-1):
        dp[j]=max(dp[j],dp[j-f[i]]+c[i])

print(max(dp))