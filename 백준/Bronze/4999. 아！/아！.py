import sys
from collections import deque
import heapq

input = sys.stdin.readline


arr1 = list(map(str, input().rstrip()))
arr2 = list(map(str, input().rstrip()))

if len(arr1) >= len(arr2):
    print("go")
else:
    print("no")
