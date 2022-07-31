N,M= map(int, input().split())
G=[set() for _ in range(N)]
for _ in range(M):
    U,V= map(int, input().split())
    U-=1
    V-=1
    G[U].add(V)
    G[V].add(U)

ans=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            if i in G[j] and j in G[k] and k in G[i]:
                ans+=1

print(ans)