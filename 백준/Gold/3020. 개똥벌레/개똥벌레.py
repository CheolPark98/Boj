import sys
from collections import deque
import heapq
import math
from bisect import bisect_left

input = sys.stdin.readline

n, h = map(int, input().split())

top, bot = [], []
for i in range(n):
    if i % 2 == 1:
        top.append(int(input()))
    else:
        bot.append(int(input()))
top.sort()
bot.sort()
mn = int(1e9)
mncnt = 0

for i in range(1, h + 1):

    b, t = bisect_left(bot, i), bisect_left(top, h - i + 1)
    sm = n - b - t

    if sm < mn:
        mn = sm
        mncnt = 1
    elif sm == mn:
        mncnt += 1


print(mn, mncnt)
