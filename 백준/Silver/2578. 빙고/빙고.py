import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

arr = []
board = [0] * 25
v = [0] * 25

for i in range(5):
    arr.extend(list((map(int, input().split()))))

for i in range(25):
    board[arr[i] - 1] = i

speak = []

for i in range(5):
    speak.extend((map(int, input().split())))


def row_check(idx, v):
    row = idx // 5
    cnt = 0
    for i in range(row * 5, row * 5 + 5):
        if v[i] == 1:
            cnt += 1
    if cnt == 5:
        return 1

    return 0


def col_check(idx, v):
    col = idx % 5
    cnt = 0
    for i in range(col, 25, 5):
        if v[i] == 1:
            cnt += 1
    if cnt == 5:
        return 1
    return 0


def cross_check1(idx, v):
    cnt = 0

    for i in range(0, 25, 6):
        if v[i] == 1:
            cnt += 1
    if cnt == 5:
        return 1
    return 0


def cross_check2(idx, v):

    cnt = 0
    for i in range(4, 23, 4):
        if v[i] == 1:
            cnt += 1
    if cnt == 5:
        return 1
    return 0


bingo = 0

for num in speak:
    idx = board[num - 1]
    v[idx] = 1

    bingo += col_check(idx, v)
    bingo += row_check(idx, v)

    if idx == 12:
        bingo += cross_check1(idx, v)
        bingo += cross_check2(idx, v)
    elif idx % 6 == 0:
        bingo += cross_check1(idx, v)
    elif idx % 4 == 0:
        bingo += cross_check2(idx, v)

    if bingo >= 3:
        print(speak.index(num)+1)
        break
