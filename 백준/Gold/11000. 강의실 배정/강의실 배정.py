import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

arr.sort()

c = [arr[0][1]]

for i in range(1, n):
    if arr[i][0] < c[0]:
        heapq.heappush(c, arr[i][1])
    else:
        heapq.heappop(c)
        heapq.heappush(c, arr[i][1])

print(len(c))
