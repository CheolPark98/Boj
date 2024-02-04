import sys
import heapq
import math

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))


def bs(t):
    s = 0
    e = len(lis) - 1
    while s <= e:
        m = (s + e) // 2

        if lis[m] == t:
            return m
        elif lis[m] < t:
            s = m + 1
        else:
            e = m - 1
    return s


lis = [arr[0]]

for e in arr:
    if lis[-1] < e:
        lis.append(e)
    else:
        lis[bs(e)] = e

print(len(lis))
