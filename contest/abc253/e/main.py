def print_func_info(func):
    def wrapper(*args, **kwargs):
        print(f"executing {func}")
        for arg in args:
            print(f":param {type(arg)} {arg}")
        results = func(*args, **kwargs)
        for result in results:
            print(f":return: {result}")
        return results
    return wrapper


MOD = 998244353
N, M, K = map(int, input().split())

dp = [[0]*(1+M) for _ in range(N)]

if K == 0:
    ans = 1
    for i in range(N):
        ans *= M
        ans %= MOD
    exit(print(ans))

for j in range(M):
    dp[0][j+1] = 1

for i in range(N-1):
    ruiseki = [0]*(M+1)
    for j in range(M):
        ruiseki[j+1] += (ruiseki[j]+dp[i][j+1]) % MOD
    for j in range(M):
        dp[i+1][j+1] = ruiseki[M] - \
            (ruiseki[j+K if j+K <= M else M] -
             ruiseki[j+1-K if j+1-K >= 0 else 0])
        dp[i+1][j+1] %= MOD
print(sum(dp[N-1]) % MOD)
