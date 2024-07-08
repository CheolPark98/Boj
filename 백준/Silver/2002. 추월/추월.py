import sys
import heapq
import math
import copy
from collections import deque
from itertools import permutations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr1 = [input().rstrip() for i in range(N)]
arr2 = [input().rstrip() for i in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if arr1[i] == arr2[j]:
            for a in arr1[:i]:
                if a not in arr2[:j]:
                    # print(arr1[i], arr2[j], arr1[:i], arr2[:j])
                    cnt += 1
                    break


print(cnt)
# print(arr1[:1])
