import sys
from collections import deque
import heapq
import copy

input=sys.stdin.readline

n,m=map(int,input().split())

edges=[]

for i in range(m):
    a,b,w=map(int,input().split())

    edges.append((w,a,b))

edges.sort()

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
    
sm=[]
for e in edges:
    w,a,b=e
    if find(a)!=find(b):
        union(a,b)
        sm.append(w)

print(sum(sm)-max(sm))