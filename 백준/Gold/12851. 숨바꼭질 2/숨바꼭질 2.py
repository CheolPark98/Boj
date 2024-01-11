from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

v = [0] * 200001


def bfs():
    ans_sec = 100001
    ans_cnt = 0
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if v[x] > ans_sec:
            break
        if x == m:
            if ans_sec == 100001:
                ans_sec = v[x]
            if v[x] == ans_sec:
                ans_cnt += 1
            continue

        for i in (x + 1, x - 1, x * 2):
            if 0 <= i <= 200000 and (v[i] == 0 or v[i] == v[x] + 1):
                v[i] = v[x] + 1
                q.append(i)
    return ans_sec, ans_cnt


a, b = bfs()
print(a)
print(b)
