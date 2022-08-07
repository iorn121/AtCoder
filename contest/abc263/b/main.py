N= int(input())
P=list(map(int, input().split()))

par=[i for i in range(N)]
for i,p in enumerate(P,1):
    p-=1
    par[i]=p
now=N-1
cnt=0
while par[now]!=now:
    # print(now,par[now])
    cnt+=1
    now=par[now]
print(cnt)