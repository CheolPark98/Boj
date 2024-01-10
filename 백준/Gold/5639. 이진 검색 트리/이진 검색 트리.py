import sys
from collections import deque
import heapq
sys.setrecursionlimit(10 ** 9)
arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break


def post(s, e):
    if s > e:
        return
    m = e + 1
    for i in range(s + 1, e + 1):
        if arr[i] > arr[s]:
            m = i
            break
    post(s + 1, m - 1)
    post(m, e)
    print(arr[s])


post(0, len(arr) - 1)
