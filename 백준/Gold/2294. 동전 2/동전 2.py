from collections import deque
import sys

n, k = map(int, input().split())
s = set()
for i in range(n):
    s.add(int(input()))

inf = k + 1
dp = [inf] * (k + 1)
dp[0] = 0

for i in s:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] = min(dp[j], dp[j - i] + 1)
          
ans=dp[k]
if ans==inf:
    ans=-1
print(ans)