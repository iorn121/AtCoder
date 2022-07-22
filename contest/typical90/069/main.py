N, K = map(int, input().split())
MOD = 10**9+7
if K == 1:
    if N == 1:
        print(1)
    else:
        print(0)
elif K == 2:
    if N == 1 or N == 2:
        print(2)
    else:
        print(0)
else:
    if N == 1:
        print(K)
    elif N == 2:
        print(K*(K-1) % MOD)
    else:
        print(K*(K-1) % MOD*pow(K-2, N-2, MOD) % MOD)
