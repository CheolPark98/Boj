import sys
from collections import deque
import heapq
import math

input = sys.stdin.readline

n = int(input())
tree = [[] for i in range(n)]

arr = list(map(int, input().split()))
r = 0
for i in range(n):
    if arr[i] == -1:
        r = i
    else:
        tree[arr[i]].append(i)

flag = 0
m = int(input())
if m == 0:
    tree[0] = []
if m == r:
    flag = 1
for i in range(n):
    if m in tree[i]:
        tree[i].pop(tree[i].index(m))


cnt = 0


def tra(x):
    global cnt
    if len(tree[x]) == 0 and flag == 0:
        cnt += 1
    else:
        for i in tree[x]:
            tra(i)


tra(r)

print(cnt)
