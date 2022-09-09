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


N, M, K = map(int, input().split())

MOD = 998244353

# dp[i][j] i番目までみて、合計がjになる
dp = [[0]*(3001) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(i-1, M*i+1):
        for k in range(1, M+1):
            dp[i][j+k] += dp[i-1][j]
            dp[i][j+k] %= MOD
# print(dp)
print(sum(dp[N][:K+1]) % MOD)
