N, K, M = map(int, input().split())

mod = 998244353

powN = pow(K, N, mod-1)

ans = pow(M, powN, mod)

if M % mod == 0:
    ans = 0
print(ans)
