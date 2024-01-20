from collections import deque
import sys
import heapq
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
h = []
c = []
cd = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            h.append((i, j))
        elif arr[i][j] == 2:
            cd.append([])
            c.append((i, j))

for i in range(len(c)):
    x, y = c[i]
    for j, k in h:
        cd[i].append(abs(x - j) + abs(y - k))
v = [0] * len(c)
ans = int(1e9)

for chi in combinations(cd, m):
    ans_arr = [999] * len(h)
    for i in range(m):
        for j in range(len(h)):
            ans_arr[j] = min(chi[i][j], ans_arr[j])
    ans = min(ans, sum(ans_arr))

print(ans)
