N= int(input())
A=list(map(int, input().split()))
MOD= 998244353
ans=N
for choice in range(2,N+1):
    dp=[[0]*choice for _ in range(choice+1)]
    dp[0][0]=1
    for a in A:
        ndp=[dp[i][:] for i in range(choice+1)]
        for used in range(1,choice+1):
            for x in range(choice):
                ndp[used][(x+a)%choice]+=dp[used-1][x]
                ndp[used][(x+a)%choice]%=MOD
        dp=ndp

    # print(dp)
    ans+=dp[choice][0]
    ans%=MOD
print(ans)