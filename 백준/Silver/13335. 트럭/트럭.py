import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, W, L = map(int, input().split())

q = list(map(int, input().split()))
wq = []
lq = []
cnt = 0
while q or wq:
    cnt += 1
    # print(sum(wq), q[0])
    if q:
        if sum(lq) + q[0] <= L:
            # print(1)
            truck = q.pop(0)
            wq.insert(0, 0)
            lq.insert(0, truck)

    for i in range(len(wq)):
        wq[i] += 1
        if wq[i] == W:
            wq.pop(i)
            lq.pop(i)
        # print(wq, lq, q, cnt)
print(cnt + 1)
