import sys
import heapq
import math
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l = 0
r = n - 1
ansidx = [l, r]
ans = abs(arr[l] + arr[r])
while l < r:
    sum = arr[l] + arr[r]

    if abs(sum) < ans:
        ans = abs(sum)
        ansidx[0] = l
        ansidx[1] = r
        if sum == 0:
            break
    if sum > 0:
        r -= 1
    else:
        l += 1
print(arr[ansidx[0]], arr[ansidx[1]])
