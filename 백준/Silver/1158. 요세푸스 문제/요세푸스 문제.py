import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

people = list(range(1, N + 1))
result = []
idx = 0

while people:
    idx = (idx + K - 1) % len(people)
    result.append(people.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")
