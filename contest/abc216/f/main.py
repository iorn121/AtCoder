N=int(input())
A=list(map(int,input().split()))
A_max=max(A)
B=list(map(int,input().split()))
MOD=998244353

AB=[(a,b) for a,b in zip(A,B)]
AB.sort(reverse=True)

dp=[0]*(A_max+1)
dp[0]=1
ans=0
while AB:
    a,b=AB.pop()
    ndp=dp[:]
    for i in range(A_max+1):
        if i>=b:
            ndp[i]+=dp[i-b]
            ndp[i]%=MOD
        if i+b<=a:
            ans+=dp[i]
            ans%=MOD
    dp=ndp[:]
    # print(dp[:10])
print(ans)