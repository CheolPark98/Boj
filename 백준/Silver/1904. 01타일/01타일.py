import sys
import heapq

input = sys.stdin.readline


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
dp[1] = 1
dp[0] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
