import sys
import heapq
from collections import Counter

input = sys.stdin.readline

S = list(map(str, input().rstrip()))
T = list(map(str, input().rstrip()))

res = 0
while T:
    #print(T)
    if T[-1] == "B":
        T.pop()
        T = T[::-1]
    elif T[-1] == "A":
        T.pop()
    if T == S:
        res = 1
        break
print(res)
