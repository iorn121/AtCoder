N,M= map(int, input().split())
lower_check=[0]*N
G=[[] for _ in range(N)]
for _ in range(M):
    A,B = map(int, input().split())
    A -= 1
    B-= 1
    if A>B:
        A,B= B, A
    G[A].append(B)
    G[B].append(A)
    lower_check[B]+=1

ans=0
for i in range(N):
    if lower_check[i]==1:
        ans+=1
print(ans)