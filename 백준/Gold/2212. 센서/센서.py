import sys
import heapq
from collections import Counter

input = sys.stdin.readline

N = int(input())
K = int(input())

arr = list(map(int, input().split()))

arr.sort()

distance = []
for i in range(1, N):
    distance.append(arr[i] - arr[i - 1])

distance.sort()
print(sum(distance[: N - K]))
