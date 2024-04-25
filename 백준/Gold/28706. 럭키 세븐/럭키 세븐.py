import sys
import heapq
from collections import Counter

input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    s = {1}
    for i in range(n):
        newSet = set()
        arr = list(map(str, input().split()))
        for i in s:
            if arr[0] == "+":
                newSet.add((i + int(arr[1])) % 7)
            else:
                newSet.add((i * int(arr[1])) % 7)
            if arr[2] == "+":
                newSet.add((i + int(arr[3])) % 7)
            else:
                newSet.add((i * int(arr[3])) % 7)
        s = newSet
    if 0 in s:
        print("LUCKY")
    else:
        print("UNLUCKY")
