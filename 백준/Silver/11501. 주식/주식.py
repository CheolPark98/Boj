import sys
import heapq
from collections import Counter

input = sys.stdin.readline

for i in range(int(input())):
    N=int(input())
    arr=list(map(int,input().split()))
    money=0
    maxPrice=0
    for i in range(len(arr)-1,-1,-1):
        if maxPrice<arr[i]:
            maxPrice=arr[i]
        else:
            money+=maxPrice-arr[i]
    print(money)


