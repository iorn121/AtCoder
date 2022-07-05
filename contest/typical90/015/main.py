N = int(input())

factorial = [1]*(N+1)
factorial_inv = [1]*(N+1)
MOD = 10**9+7
for i in range(1, N+1):
    factorial[i] = (factorial[i-1]*i) % MOD
factorial_inv[-1] = pow(factorial[-1], MOD-2, MOD)
for i in range(N, 0, -1):
    factorial_inv[i-1] = (factorial_inv[i]*i) % MOD
# print(U)


def nCk(n: int, k: int):
    if k < 0 or n-k < 0:
        return 0
    else:
        return (factorial[n]*factorial_inv[k] % MOD)*factorial_inv[n-k] % MOD


for i in range(1, N+1):
    ans = 0
    for j in range(1, N+1):
        p = N-(i-1)*(j-1)
        if p < j:
            break
        ans += (nCk(p, j)) % MOD
        ans %= MOD
        # print(f"j: {j}, ans: {ans}")
    print(ans)
