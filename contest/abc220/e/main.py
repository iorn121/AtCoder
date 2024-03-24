N,D=map(int, input().split())
ans=0
MOD=998244353
for i in range(N):
    if 2*i<D:
        continue
    left,right=max(0,D-i),min(i,D)
    new_ans=0
    if left==0:
        new_ans+=2*pow(2,D-1,MOD)
        left+=1
    if right==D:
        new_ans+=2*pow(2,D-1,MOD)
        right-=1
    # print(new_ans,left,right)
    new_ans+=2*pow(2,D-2,MOD)*(right-left+1)%MOD
    ans=2*ans+new_ans
    ans%=MOD
    # print(ans)
print(ans)