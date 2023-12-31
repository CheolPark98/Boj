arr=[0,1,3]+[0]*998
n= int(input())

for i in range(3,n+1):
    arr[i]= arr[i-1]+2*arr[i-2]

print(arr[n]%10007)