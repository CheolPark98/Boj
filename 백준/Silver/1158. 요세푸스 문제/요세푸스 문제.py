import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

i = 0
v = [0] * N
result = []
for j in range(N):

    cnt = 0
    while cnt < K:
        if v[(i + 1) % N] == 1:
            i = (i + 1) % N
        else:
            cnt += 1
            i = (i + 1) % N

    v[i] = 1
    if i == 0:
        result.append(N)
    else:
        result.append(i)


print("<" + ", ".join(map(str, result)) + ">")
