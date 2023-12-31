from collections import deque
import sys
from itertools import combinations

N, M = map(int, input().split())

def bfs(s):
    q = deque()
    q.append(s)
    v = [0] * 200001
    while q:
        a = q.popleft()
        if a == M:
            break
        for i in (a - 1, a + 1, a * 2):
            if 0 <= i <= 200000:
                if v[i] == 0:
                    v[i] = v[a] + 1
                    q.append(i)
    return v[M]

print(bfs(N))