import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

s = 1
e = arr[-1] - arr[0]

result = 0

while s <= e:
    m = (s + e) // 2

    curent = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if curent + m <= arr[i]:
            cnt += 1
            curent = arr[i]

    if c <= cnt:
        s = m + 1
        result = m
    else:
        e = m - 1
print(result)
