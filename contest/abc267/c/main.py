N,M= map(int, input().split())
A= list(map(int, input().split()))

total=0
ans=0
for i in range(M):
    ans+=(i+1)*A[i]
    total+=A[i]
tmp=ans
for i in range(N-M):
    tmp=tmp-total+A[i+M]*M
    total=total-A[i]+A[i+M]
    # print(tmp,total)
    ans=max(ans,tmp)
print(ans)