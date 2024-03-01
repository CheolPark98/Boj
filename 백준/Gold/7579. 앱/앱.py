import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
b = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

dp = [[0 for i in range(sum(c) + 1)] for i in range(n+1)]
mn = sum(c)
for i in range(1, n + 1):
    for j in range( sum(c) + 1):
        if j < c[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c[i]] + b[i])
        if dp[i][j] >= m:
            mn = min(j, mn)
if m == 0:
    print(0)
else:
    print(mn)
