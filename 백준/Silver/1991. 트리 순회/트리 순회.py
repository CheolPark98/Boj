from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

arr = {}

for i in range(n):
    p, l, r = map(str, input().split())
    arr[p] = [l, r]


def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(arr[root][0])
        preorder(arr[root][1])


def inorder(root):
    if root != ".":
        inorder(arr[root][0])
        print(root, end="")
        inorder(arr[root][1])


def postorder(root):
    if root != ".":
        postorder(arr[root][0])
        postorder(arr[root][1])
        print(root, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
