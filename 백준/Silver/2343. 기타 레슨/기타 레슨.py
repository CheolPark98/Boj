import sys
import heapq
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = sum(arr)
res = e
#print(arr)


def insertc(size):
    cnt = 0
    disc = 0
    for i in range(N):
        if disc + arr[i] <= size:
            disc += arr[i]
        else:
            if cnt == M - 1:
                return False
            cnt += 1
            if arr[i] > size:
                return False
            disc = arr[i]
     #   print(cnt, disc)
    return True


# 2, 2, 2, 3, 3, 4, 7, 7, 8, 9, 10, 12

while s <= e:
    m = (s + e) // 2
    #print(m, s, e, insertc(m))
    if insertc(m) == True:
        e = m - 1
        if m < res:
            res = m
    else:
        s = m + 1

print(res)
