import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for i in range(6)]

maxh, maxw = 0, 0
maxh_idx, maxw_idx = 0, 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if arr[i][1] > maxw:
            maxw = arr[i][1]
            maxw_idx = i
    if arr[i][0] == 3 or arr[i][0] == 4:
        if arr[i][1] > maxh:
            maxh = arr[i][1]
            maxh_idx = i

sw = abs(arr[(maxh_idx - 1) % 6][1] - arr[(maxh_idx + 1) % 6][1])
sh = abs(arr[(maxw_idx - 1) % 6][1] - arr[(maxw_idx + 1) % 6][1])

print((maxh * maxw - sw * sh) * N)
