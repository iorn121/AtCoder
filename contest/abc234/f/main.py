import collections
MOD=998244353
S=input()
N=len(S)
factorial=[1]*(N+1)
inv_factorial=[1]*(N+1)
for i in range(1,N+1):
    factorial[i]=factorial[i-1]*i%MOD
    inv_factorial[i]=pow(factorial[i],MOD-2,MOD)
ans=0
alpha=[0]*26
for s in S:
    alpha[ord(s)-ord('a')]+=1
dp=[[0]*(N+1) for _ in range(27)]
dp[0][0]=1
ans=0
for i in range(26):
    for j in range(N+1):
        for k in range(min(j+1,alpha[i]+1)):
            dp[i+1][j]+=factorial[j]*inv_factorial[k]%MOD*inv_factorial[j-k]%MOD*dp[i][j-k]%MOD
            dp[i+1][j]%=MOD
    # print(dp[i+1])
for i in range(1,N+1):
    ans+=dp[26][i]
    ans%=MOD
print(ans)