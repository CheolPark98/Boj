import sys
import heapq
import math

input = sys.stdin.readline

n, k = map(int, input().split())

jew = []

for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jew, (m, -v))

bag = []

for i in range(k):
    c = int(input())
    bag.append(c)
bag.sort()
res = 0

tmp = []


def solve():
    global res
    for c in bag:
        while jew:
            if jew[0][0] <= c:
                w, v = heapq.heappop(jew)
                heapq.heappush(tmp, (v, w))
                
            else:
                break
        if tmp:
            res -= heapq.heappop(tmp)[0]


solve()
print(res)
