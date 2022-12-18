X=list(map(int, input().split()))
MOD= 998244353
ans=(X[0]*X[1]*X[2]-X[3]*X[4]*X[5])%MOD
print(ans)