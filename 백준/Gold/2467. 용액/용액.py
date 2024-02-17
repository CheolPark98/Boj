import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.sort()
l, r = 0, n - 1
res = [0, 0]
res[0], res[1] = arr[l], arr[r]
mnsm = abs(res[0]+res[1])
while l < r:
    sm = arr[l] + arr[r]
    if mnsm > abs(sm):
        mnsm = abs(sm)

        res[0], res[1] = arr[l], arr[r]
        if sm == 0:
            break
    if sm > 0:
        r -= 1
    else:
        l += 1


print(res[0], res[1])
