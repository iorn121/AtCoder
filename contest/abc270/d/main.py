

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


N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [0]*(N+1)
for s in range(1, N+1):
    for a in A:
        if s-a < 0:
            continue
        dp[s] = max(dp[s], s-dp[s-a])
    # print(s, dp[s])

print(dp[N])
