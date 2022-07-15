N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
MOD = 10**9+7

sumA = [sum(A[i]) for i in range(N)]
ans = 1
for i in range(N):
    ans *= (sum(A[i]) % MOD)
    ans %= MOD
print(ans)
