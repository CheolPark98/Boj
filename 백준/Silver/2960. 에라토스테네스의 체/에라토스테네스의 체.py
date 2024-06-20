import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

arr = [i for i in range(2, N + 1)]
cnt = 0
while cnt != K:
    tmp = []
    prime_num = arr[0]
    for i in range(len(arr)):
        if arr[i] % prime_num == 0:
            tmp.append(arr[i])
            cnt += 1
            if cnt == K:
                print(arr[i])
                break
    for i in range(len(tmp)):
        arr.remove(tmp[i])
