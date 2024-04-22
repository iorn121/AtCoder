MOD = 998244353

def add(a, b):
    c = a + b
    if c >= MOD:
        c -= MOD
    return c

def sub(a, b):
    c = a - b
    if c < 0:
        c += MOD
    return c

def main():
    N, K = map(int, input().split())
    rng = [list(map(int, input().split())) for _ in range(K)]

    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = sub(dp[2], dp[1])

    for i in range(1, N+1):
        if i > 1:
            dp[i] = add(dp[i], dp[i-1])
        for l, r in rng:
            if i + l <= N:
                dp[i + l] = add(dp[i + l], dp[i])
            if i + r + 1 <= N:
                dp[i + r + 1] = sub(dp[i + r + 1], dp[i])
    print(dp[N])

if __name__ == "__main__":
    main()