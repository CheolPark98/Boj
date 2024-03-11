import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())

arr = list(map(int, input().split()))

lis = [arr[0]]
dp = [(0, arr[0])]
for i in range(1, n):
    idx = 0
    if lis[-1] < arr[i]:
        lis.append(arr[i])
        dp.append((len(lis) - 1, arr[i]))
    else:
        for j in range(len(lis)):
            if lis[j] < arr[i]:
                idx += 1

            else:
                break
        lis[idx] = arr[i]
        dp.append((idx, arr[i]))

idx = len(lis) - 1
res = []
for i in range(n - 1, -1, -1):
    if dp[i][0] == idx:
        res.append(dp[i][1])
        idx -= 1
print(len(lis))
print(*res[::-1])
