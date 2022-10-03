N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
ans=0
check=A[0][:]
for i in range(N-1):
    for j in range(N):
        check[j]=check[j]^A[i+1][j]
print(ans)