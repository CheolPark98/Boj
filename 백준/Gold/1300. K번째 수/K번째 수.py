import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
k = int(input())

s,e=1,k

while s<=e:
    m=(s+e)//2

    tmp=0

    for i in range(1,n+1):
        tmp += min(m//i,n)
    if tmp>=k:
        ans=m
        e=m-1
    else:
        s=m+1
print(ans)