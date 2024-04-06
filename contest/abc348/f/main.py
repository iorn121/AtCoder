N,M=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
B=[[-1]*M for _ in range(N)]


cnt=0
for j in range(M):
    cvt={}
    for i in range(N):
        if A[i][j] not in cvt:
            cvt[A[i][j]]=cnt
            cnt+=1
        B[i][j]=cvt[A[i][j]]
# print(B)

bit=[0]*N
for i in range(N):
    for j in range(M):
        bit[i]+=1<<B[i][j]
# print(bit)
ans=0
for i in range(N-1):
    for j in range(i+1,N):
        # print(bit[i],bit[j],bit[i]&bit[j],(bit[i]&bit[j]).bit_count())
        if (bit[i]&bit[j]).bit_count()%2==1:
            ans+=1
print(ans)