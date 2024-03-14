import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    heapq.heappush(arr, int(input()))
res = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    c = a + b
    res += c
    heapq.heappush(arr, c)
print(res)
