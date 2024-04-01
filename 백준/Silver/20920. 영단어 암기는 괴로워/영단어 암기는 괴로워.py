import sys
import heapq
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())

words = {}
for i in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    if word in words:
        words[word][0] += 1
    else:
        words[word] = [1, len(word), word]
ans = sorted(words.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))
for i in ans:
    print(i[0])
