N, K, M = map(int, input().split())

mod = 998244353

powN = pow(K, N, mod-1)

ans = pow(M, powN, mod)

if ans % mod == 0:
    ans = 0
print(ans)
