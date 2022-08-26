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


N, M = map(int, input().split())
move = list(map(int, input().split()))
dxy = [(move[2*i], move[2*i+1]) for i in range(3)]
MOD = 998244353
check = set([tuple(map(int, input().split())) for _ in range(M)])

dp = [[1]]
for i in range(N):
    new_dp = [[0]*(i+2) for _ in range(i+2)]
    for a in range(i+1):
        for b in range(i+1):
            if a+b > i:
                continue
            x = dxy[0][0]*a+dxy[1][0]*b+dxy[2][0]*(i-a-b)
            y = dxy[0][1]*a+dxy[1][1]*b+dxy[2][1]*(i-a-b)
            for j, (dx, dy) in enumerate(dxy):
                if not ((x+dx, y+dy) in check):
                    new_dp[a+(1 if j == 0 else 0)][b +
                                                   (1 if j == 1 else 0)] += dp[a][b]
                    new_dp[a+(1 if j == 0 else 0)][b +
                                                   (1 if j == 1 else 0)] %= MOD
    dp = new_dp
print(sum(sum(x) for x in dp) % MOD)
