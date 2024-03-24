import sys
import heapq
from collections import Counter

input = sys.stdin.readline

arr = list(map(str, input().rstrip()))

for i in range(len(arr)):
    if "a" <= arr[i] <= "z":
        arr[i] = arr[i].upper()
    else:
        arr[i] = arr[i].lower()

for i in range(len(arr)):
    print(arr[i], end="")
