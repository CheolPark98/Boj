import sys
input = sys.stdin.readline

n, B = 2, int(input())
A = [[1,1],[1,0]]

def power(a,b,n):
    cal = []
    for i in range(n):
        temp = []
        for j in range(n):
            num = 0
            for k in range(n):
                num += a[i][k] * b[k][j]
            temp.append(num%1000000007)
        cal.append(temp)
    return cal
    # 행렬의 곱셉을 함수화 해보았다.

def dac(s,b):
    if b == 1:
        return s
    
    a = dac(s,b//2)
    
    cal = power(a,a,n)
    
    result = []
    if b % 2:
        result = power(cal,A,n)
    else:
        result = cal
        
    return result
print(dac(A,B)[0][1])