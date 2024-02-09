import sys
import heapq
import math
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
v = [0] * n
for i in range(n):
    sm = arr[i]
    for j in range(i + 1, n):
        sm += arr[j]
        for k in range(n):
            if sm == arr[k] and v[k] == 1:
                break
            if sm == arr[k] and v[k] == 0 and k!=j and k!=i:
                cnt += 1
                v[k] = 1
                # print(sm)
        sm -= arr[j]

print(cnt)
