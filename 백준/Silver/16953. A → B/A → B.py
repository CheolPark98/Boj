import sys
from collections import deque
import heapq

N, m = map(int, input().split())
INF = int(1e9)

mincnt = INF


def solve(n, cnt):
    global mincnt
    if n == m:
        if mincnt > cnt:
            mincnt = cnt
    if n > m:
        return

    solve(n * 2, cnt + 1)
    n2 = int(str(n) + "1")
    solve(n2, cnt + 1)


solve(N, 1)
if mincnt == INF:
    print(-1)
else:
    print(mincnt)
