import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

lis = [arr[0]]
dp = [(0, arr[0])]


def bs(x):
    s = 0

    e = len(lis) - 1
    while s <= e:
        m = (s + e) // 2
        if lis[m] == x:
            return m
        elif lis[m] > x:
            e = m - 1
        else:
            s = m + 1
    return s


for i in range(1, n):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
        dp.append((len(lis) - 1, arr[i]))
    else:
        idx = bs(arr[i])
        lis[idx] = arr[i]
        dp.append((idx, arr[i]))

res = []
idx = len(lis) - 1

for i in range(n - 1, -1, -1):

    if dp[i][0] == idx:
        res.append(dp[i][1])
        idx -= 1
print(len(lis))
print(*res[::-1])
