import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

c = int(input())

s = 0
e = max(arr)
std = 0
while s <= e:
    m = (s + e) // 2
    sm = 0
    for i in range(n):
        sm += min(arr[i], m)
    #print(s, e, sm)

    if sm > c:
        e = m - 1
    else:
        s = m + 1
        std = m
print(std)
