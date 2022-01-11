N = int(input())
A = list(map(int, input().split()))

MOD = 998244353

A.sort()

ans = 0
tmp = 0
for i in range(N):
    ans = (ans+A[i]**2) % MOD
    ans = (ans+tmp*A[i]) % MOD
    tmp = (A[i]+tmp*2) % MOD

print(ans)
