import sys
from collections import deque
import heapq

input = sys.stdin.readline

arr = list(input().strip())
arr.append(" ")

stack = []
result = ""
flag = 0
for i in arr:

    if i == "<":
        flag = 1
        while stack:
            result += stack.pop()
    stack.append(i)

    if i == ">":
        while stack:
            result += stack.pop(0)
        flag = 0

    elif i == " " and flag == 0:
        stack.pop()
        while stack:
            result += stack.pop()
        result += " "
print(result)
