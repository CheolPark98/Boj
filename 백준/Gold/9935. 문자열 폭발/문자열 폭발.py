from collections import deque
import sys

input = sys.stdin.readline

s = input().rstrip()
ex = input().rstrip()
stack = []

for i in range(len(s)):
    stack.append(s[i])
    if "".join(stack[-len(ex) :]) == ex:
        for j in range(len(ex)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    for i in stack:
        print(*i, end="")
