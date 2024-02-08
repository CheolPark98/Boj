import sys
import heapq
import math
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

e = 0
sum = 0
l = 100000

for s in range(n):
    while e < n and sum < m:
        sum += arr[e]
        e += 1
    if sum >= m and e - s < l:
        l = e - s
    sum -= arr[s]
if l==100000:
    print(0)
else:
    print(l)