from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

tp = set(input().split()[1:])

parties = []
for i in range(m):
    parties.append(set(input().split()[1:]))

for i in range(m):
    for party in parties:
        if tp & party:
            tp = tp.union(party)
cnt = 0
for i in range(1):
    for party in parties:
        if party & tp:
            continue
        cnt += 1

print(cnt)
