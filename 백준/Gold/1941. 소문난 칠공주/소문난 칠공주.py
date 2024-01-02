from collections import deque
import sys

arr = [list(map(str, sys.stdin.readline().strip())) for i in range(5)]
result = []
v = [[0 for i in range(5)] for j in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


v2 = [0] * 25
ans_num = 0


def dfs(n, cnt, sc):
    global ans_num
    if n == 25:
        if cnt == 7 and sc >= 4:
            if check():
                ans_num += 1
        return
    v[n // 5][n % 5] = 1
    dfs(n + 1, cnt + 1, sc + int(arr[n // 5][n % 5] == "S"))
    v[n // 5][n % 5] = 0
    dfs(n + 1, cnt, sc)


def check():
    flag = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i, j)


def bfs(x, y):
    q = deque()
    vv = [[0 for i in range(5)] for j in range(5)]
    vv[x][y] = 1
    q.append((x, y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if v[nx][ny] == 1 and vv[nx][ny] == 0:
                    q.append((nx, ny))
                    vv[nx][ny] = 1
                    cnt += 1
    return cnt == 7


dfs(0, 0, 0)
print(ans_num)
