from collections import deque
import sys
import heapq
from itertools import combinations

input = sys.stdin.readline

a, b = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(a)]


def solve(n, lst):
    if n == 1:
        return lst
    tmp = solve(n // 2, lst)
    if n % 2 == 0:
        return mm(tmp, tmp)
    else:
        return mm(mm(tmp, tmp), arr)


def mm(lst1, lst2):
    res = [[0] * a for i in range(a)]
    for i in range(a):
        for j in range(a):
            for k in range(a):
                res[i][j] += lst1[i][k] * lst2[k][j] %1000
    return res


res = solve(b, arr)
for i in range(a):
    for j in range(a):
        res[i][j] %= 1000
for i in res:
    print(*i)
