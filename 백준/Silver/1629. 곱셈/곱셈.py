from collections import deque
import sys
import heapq
from itertools import combinations

input = sys.stdin.readline

a, b, c = map(int, input().split())


def solve(n, m, k):
    if m == 1:
        return n % k
    else:
        h = solve(n, m // 2, k)
        if m % 2 == 0:
            return (h * h) % k
        else:
            return (h * h * n) % k


print(solve(a, b, c))
