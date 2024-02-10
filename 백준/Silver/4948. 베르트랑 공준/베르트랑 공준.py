import sys
from collections import deque
import heapq
import math

input = sys.stdin.readline


def pm(n):
    pn = []
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    pi = 2
    while pi**2 <= n:
        if arr[pi]:

            for i in range(pi**2, n + 1, pi):
                arr[i] = False
        pi += 1

    for i in range(n + 1):
        if arr[i]:
            pn.append(i)
    return len(pn)


while 1:
    n = int(input())
    if n == 0:
        break
    print(pm(2 * n) - pm(n))
