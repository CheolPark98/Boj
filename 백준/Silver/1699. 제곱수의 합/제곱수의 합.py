n = int(input())
arr = [0] * 330
for i in range(1, len(arr) + 1):
    arr[i - 1] = i * i
dp = [100001] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in arr:
        if i - j >= 0:
            dp[i] = min(dp[i - j] + 1, dp[i])

print(dp[n])