n=int(input())
m=int(input())
def dfs(c):
    global cnt
    cnt+=1
    v[c]=1

    for n in adj[c]:
        if not v[n]:
            dfs(n)

adj=[[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

cnt=0

v=[0]*(n+1)
dfs(1)
print(cnt-1)