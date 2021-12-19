from functools import reduce
from operator import mul
H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())


MOD = 998244353
W %= MOD
H %= MOD
ans = 0
x = 1

for tate in range(K+1):
    yoko = K-tate
    x *= yoko
    x //= tate+1
    if tate == 0:
        if y1 != y2:
            continue
        else:
            ans += (pow(W-1, yoko-1) % MOD)
    elif yoko == 0:
        if x1 != x2:
            continue
        else:
            ans += (pow(H-1, tate-1) % MOD)
    else:
        ans += (pow(W-1, yoko-1) % MOD)*(pow(H-1, tate-1) % MOD)*x
    ans %= MOD
print(ans)
