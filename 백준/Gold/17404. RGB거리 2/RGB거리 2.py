import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

INF = int(1e9)
ans = INF
for j in range(3):

    dp = [[INF, INF, INF] for i in range(n)]
    dp[0][j] = arr[0][j]
    for i in range(1, n):

        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + arr[i][2]
    for i in range(3):
        if j != i:
            ans = min(ans, dp[n - 1][i])

print(ans)
