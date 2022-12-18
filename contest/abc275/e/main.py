N,M,K = map(int, input().split())
MOD= 998244353
class NoSolution(ArithmeticError):
    pass
 
 
# ax + by = gcd(a, b) = z を求める
def extra_GCD(a, b):
    z1, z2 = a, b
    x1, y1 = 1, 0
    x2, y2 = 0, 1
    while z2:
        t = z1 // z2
        z1 -= t * z2
        x1 -= t * x2
        y1 -= t * y2
        z1, z2 = z2, z1
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    x1 = x1 % (b // z1)
    y1 = (z1 - a * x1) // b
    return x1, y1, z1
 
 
def mod_div(a, b, n):
    x, y, gcd = extra_GCD(b, n)
    if gcd == 1:
        return a * x % n
    elif a % gcd == 0:
        return x * (a // gcd) % (n // gcd)
    else:
        raise NoSolution("{} / {} (mod {})".format(a, b, n))
from collections import defaultdict
d=defaultdict(int)
dp=[[0]*(N+1) for _ in range(K+1)]
dp[0][0]=1
for i in range(K):
    dp[i+1][N]=(dp[i][N]*M)%MOD
    for j in range(N):
        for k in range(1,M+1):
            p=j+k
            if p>N:
                p=N*2-p
            dp[i+1][p]+=dp[i][j]
            dp[i+1][p]%= MOD
    # print(dp[i+1])
    # print(sum(dp[i+1]))
# print(pow(M,K),MOD,dp[K][N])
x=pow(M,K)%MOD
y=dp[K][N]%MOD
print(mod_div(y,x,MOD))