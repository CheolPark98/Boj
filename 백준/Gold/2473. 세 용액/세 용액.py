import sys
from collections import deque
import heapq
import copy

input=sys.stdin.readline

n=int(input())

arr=list(map(int,input().split()))
arr.sort()
#print(arr)

res=[0,0,0]
mn=sys.maxsize
for i in range(n-2):
    s=i+1
    e=n-1
    while s<e:
        sm=arr[i]+arr[s]+arr[e]
        if abs(sm)<mn:
            res[0],res[1],res[2]=arr[i],arr[s],arr[e]
            #print(i,s,e,sm)
            mn=abs(sm)
        if sm<0:
            s+=1
        elif sm>0:
            e-=1
        else:
            break
        
print(*res)
