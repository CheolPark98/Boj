from collections import deque
import sys
from itertools import combinations

F, S, G, U, D = map(int, input().split())
v = [0] * 1000001
v2 = []


def bfs():
    q = deque()
    q.append(S)
    while q:
        a = q.popleft()
        if a == G:
            break
        if len(v2) > 2:
            if v2[len(v2) - 1] == v2[len(v2) - 3]:
                break
        for i in (U, -D):
            if 0 < i + a <= F:
                if v[i + a] == 0 and i != 0:
                    v[i + a] = v[a] + 1
                    q.append(a + i)
                    v2.append(a + i)


a = bfs()
if v[G] == 0 and S != G:
    print("use the stairs")
else:
    print(v[G])
