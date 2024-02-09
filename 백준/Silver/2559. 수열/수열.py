import sys
import heapq
import math
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = 0
e = k - 1
sm = sum(arr[: e + 1])
mx = sm

for i in range(n - k):
    #print(sm, arr[s], arr[e])
    sm -= arr[s]
    s += 1
    e += 1
    sm += arr[e]

    if mx < sm:
        mx = sm
print(mx)
