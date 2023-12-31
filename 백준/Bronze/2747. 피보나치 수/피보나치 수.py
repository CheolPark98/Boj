from collections import deque
import sys
from itertools import combinations

arr = [0] * 46


def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if arr[n] == 0:
        arr[n] = f(n - 1) + f(n - 2)
    return arr[n]


n = int(input())
print(f(n))
