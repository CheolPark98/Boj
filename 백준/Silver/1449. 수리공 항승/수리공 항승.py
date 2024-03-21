import sys
import heapq

input = sys.stdin.readline

n, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
s = arr[0]
cnt = 1

for p in arr[1:]:
    if p in range(s, s + l):
        continue
    else:
        s = p
        cnt += 1

print(cnt)
