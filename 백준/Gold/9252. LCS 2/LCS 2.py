import sys
from collections import deque
import heapq
import copy

input=sys.stdin.readline

arr1=list(map(str,input().rstrip()))
arr2=list(map(str,input().rstrip()))


len1= len(arr1)
len2= len(arr2)
dp=[[0,'']for i in range(len2)]
dp[0][1].join('d')
for i in range(len1):
    cnt=0
    w=''
    for j in range(len2):
        if dp[j][0] > cnt:
            cnt=dp[j][0]
            w=dp[j][1]
        elif arr1[i]==arr2[j]:
            dp[j][0]=cnt+1
            dp[j][1]=w+arr2[j]
ans=max(dp)[0]
if ans==0:
    print(ans)
else:
    print(ans)
    print(max(dp)[1])

#print(dp)