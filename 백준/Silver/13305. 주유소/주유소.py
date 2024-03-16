import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
sum = 0
mn = max(cost)
for i in range(n - 1):
    mn = min(mn, cost[i])
    sum += mn * distance[i]

print(sum)
