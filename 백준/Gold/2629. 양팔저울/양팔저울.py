import sys
import heapq
import math
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))

m = int(input())
marbles = list(map(int, input().split()))
dpsize = max(max(marbles), sum(w))
dp = [0 for i in range(dpsize + 1)]

for i in range(n):
    for j in range(dpsize, 0, -1):
        if dp[j] == 1 and w[i] + j <= dpsize:

            dp[w[i] + j] = 1

        if dp[j] == 0 and j == w[i]:
            dp[j] = 1

for i in range(m):
    flag = 0
    if dp[marbles[i]] == 1:
        print("Y ", end="")
        flag = 1
    if flag == 0:
        for j in range(1, dpsize + 1):
            if j + marbles[i] > dpsize:
                break
            if dp[j] == 1 and dp[j + marbles[i]] == 1:
                print("Y", end=" ")
                flag = 1
                break
    if flag == 0:
        print("N ", end="")
