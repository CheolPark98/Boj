import sys
import heapq
from collections import Counter

input = sys.stdin.readline

word1=list(map(str,input().rstrip()))
word2=list(map(str,input().rstrip()))

ans=0

dp=[[0 for i in range(len(word2)+1)] for i in range(len(word1)+1)]

for i in range(1,len(word1)+1):
    for j in range(1,len(word2)+1):
        if word1[i-1]==word2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            ans=max(dp[i][j],ans)
print(ans)