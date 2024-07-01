import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

dp1 = [1] * N
dp2 = [1] * N
for i in range(1, N):
    if arr[i] >= arr[i - 1]:
        dp1[i] = dp1[i - 1] + 1
for i in range(1, N):
    if arr[i] <= arr[i - 1]:
        dp2[i] = dp2[i - 1] + 1

max1 = max(dp1)
max2 = max(dp2)
print(max(max1, max2))
