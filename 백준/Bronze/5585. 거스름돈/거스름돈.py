import sys
from collections import deque
import heapq
import copy

def bfs():
    cnt=0
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx= x+dx[i]
            ny=y+dy[i]
            if nx<0 or m<=nx or ny<0 or n<=ny:
                continue
            if arr[nx][ny] == 1 :
                continue
            if arr[nx][ny]==0:
                arr[nx][ny]=2
                cnt+=1
                q.append((nx,ny))
    if cnt==0:
        return 1
    return cnt


n=int(input())
n=1000-n
cnt=0
while (n>=500):
    n-=500
    cnt+=1

while (n>=100):
    n-=100
    cnt+=1
    
while (n>=50):
    n-=50
    cnt+=1

while (n>=10):
    n-=10
    cnt+=1
    
while (n>=5):
    n-=5
    cnt+=1
    
while (n>=1):
    n-=1
    cnt+=1

print(cnt)