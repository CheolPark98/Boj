import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
n.sort()
n = n[::-1]
for i in range(len(n)):
    print(n[i], end="")
