import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

g = int(input())
p = int(input())

gates = []

parent = [i for i in range(g + 1)]

for i in range(p):
    gates.append(int(input()))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


flag = 0


def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


cnt = 0

for pla in gates:
    x = find(pla)

    if x == 0:
        break
    union(x, x - 1)
    cnt += 1
print(cnt)
