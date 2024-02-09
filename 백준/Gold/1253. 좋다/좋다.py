import sys
import heapq
import math
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0

for i in range(n):
    target = arr[i]
    s, e = 0, n - 1
    while s < e:
        sm = arr[s] + arr[e]
        if sm == target:
            if s == i:
                s += 1
            elif e == i:
                e -= 1
            else:
                cnt += 1
                break
        elif target > sm:
            s += 1
        else:
            e -= 1
print(cnt)
