import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input())

color = []

for i in range(N):
    b, h = map(int, input().split())
    color.append((b, h))
paper = [[0 for j in range(100)] for i in range(100)]

for i in range(N):
    b, h = color[i]
    for j in range(b, b + 10):
        for k in range(h, h + 10):
            paper[j][k] = 1

cnt = 0

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)
