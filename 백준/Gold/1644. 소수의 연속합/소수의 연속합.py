import sys
from collections import deque
import heapq
import math

input = sys.stdin.readline

pn = []


def sieve_of_eratosthenes(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False
    pi = 2
    while pi**2 <= n:
        if p[pi]:
            for i in range(pi * 2, n + 1, pi):
                p[i] = False
        pi += 1
    for i in range(n):
        if p[i]:
            pn.append(i)


sieve_of_eratosthenes(4000000)
n = int(input())


def solve(n):
    cnt = 0
    for i in range(len(pn)):
        sum = pn[i]
        if sum == n:
            cnt += 1
            return cnt
        elif sum > n:
            return cnt
        for j in range(i + 1, len(pn)):
            sum += pn[j]
            if sum == n:
                cnt += 1
                break
            elif sum > n:
                break
    return cnt


print(solve(n))
