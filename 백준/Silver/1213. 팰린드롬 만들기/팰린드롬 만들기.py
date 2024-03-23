import sys
import heapq
from collections import Counter

input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
arr.sort()
word = Counter(arr)

ans = ""
oddword = ""
cnt = 0
for i in word:
    if word[i] % 2 != 0:
        cnt += 1
        oddword += i
    for j in range(word[i] // 2):
        ans += i
if cnt > 1:
    print("I'm Sorry Hansoo")
elif cnt == 0:
    print(ans + ans[::-1])
else:
    print(ans + oddword + ans[::-1])
