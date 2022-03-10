N = int(input())
A = list(map(int, input().split()))
A.append(0)
MOD = 10**9+7

A.sort()

ans = 1
for i in range(N):
    ans *= (A[i+1]-A[i]+1) % MOD
    ans %= MOD

print(ans)
