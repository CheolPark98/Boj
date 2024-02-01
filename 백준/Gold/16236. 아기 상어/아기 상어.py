import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    q = []
    heapq.heappush(q, (0, i, j))

    size = 2
    t = 0
    stack = -1
    while q:
        d, x, y = heapq.heappop(q)

        arr[x][y] = 0
        stack += 1
        if stack == size:
            size += 1
            stack = 0
        t += d
        q = []
        v = [[0 for _ in range(n)] for _ in range(n)]
        q2 = deque()
        q2.append((0, x, y))
        cnt = 0
        while q2:
            d, x1, y1 = q2.popleft()

            for i in range(4):
                nx, ny = dx[i] + x1, y1 + dy[i]

                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and arr[nx][ny] <= size
                    and v[nx][ny] == 0
                ):
                    v[nx][ny] = 1
                    if 1 <= arr[nx][ny] < size:
                        heapq.heappush(q, (d + 1, nx, ny))
                       
                    q2.append((d + 1, nx, ny))

    return t


for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            print(bfs(i, j))
