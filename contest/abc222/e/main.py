N,M,K=map(int,input().split())
A=list(map(int,input().split()))
MOD=998244353
G=[[] for _ in range(N)]
for i in range(N-1):
    U,V=map(int,input().split())
    U-=1
    V-=1
    G[U].append((V,i))
    G[V].append((U,i))

from collections import deque

def bfs_restore(f,t,cnt):
    q=deque([f])
    dist=[-1]*N
    dist[f]=0
    while q:
        v=q.popleft()
        for nv,eid in G[v]:
            if dist[nv]!=-1: continue
            dist[nv]=dist[v]+1
            q.append(nv)
    if dist[t]==-1: return []
    path=[t]
    while path[-1]!=f:
        v=path[-1]
        for nv,eid in G[v]:
            if dist[nv]==dist[v]-1:
                cnt[eid]+=1
                path.append(nv)
                break
    return path[::-1]

cnt=[0]*(N-1)
for f,t in zip(A,A[1:]):
    f-=1
    t-=1
    path=bfs_restore(f,t,cnt)

total=sum(cnt)
if (total+K)%2==1 or total-K<0:
    print(0)
    exit()
num=(K+total)//2
if num<0 or num>total:
    print(0)
    exit()
# print(num)
dp=[[0]*(num+1) for _ in range(N)]
dp[0][0]=1
zero=0
for i in range(N-1):
    c=cnt[i]
    if c==0:
        zero+=1
    for j in range(num+1):
        if j+c<=num and c>0:
            dp[i+1][j+c]+=dp[i][j]
            dp[i+1][j+c]%=MOD
        dp[i+1][j]+=dp[i][j]
    # print(dp[i+1])
print(dp[N-1][num]*pow(2,zero,MOD)%MOD)