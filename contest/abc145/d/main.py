def make_fact_inv(n,mod):
    fact=[1]*(n+1)
    fact_inv=[1]*(n+1)
    for i in range(1,n+1):
        fact[i]=(fact[i-1]*i)%mod
    fact_inv[n]=pow(fact[n],mod-2,mod)
    for i in range(n,0,-1):
        fact_inv[i-1]=(fact_inv[i]*i)%mod
    return fact,fact_inv


def combination(n,r):
    if n<r:
        return 0
    if n==r or r==0:
        return 1
    fact,fact_inv=make_fact_inv(n,MOD)
    return (fact[n]*fact_inv[r]*fact_inv[n-r])%MOD


X,Y=map(int,input().split())
MOD=10**9+7
if (X+Y)%3!=0 or X>2*Y or Y>2*X:
    print(0)
    exit()
total=(X+Y)//3
X_num=(total+X-Y)//2
Y_num=total-X_num

print(combination(total,X_num))
