S = input()

dp = [[0]*9 for i in range(len(S)+1)]
for i in range(len(S)+1):
    dp[i][0] = 1

mod = 10**9+7

s_list = ["c", "h", "o", "k", "u", "d", "a", "i"]
for i in range(len(S)):
    for j in range(8):
        if S[i] == s_list[j]:
            dp[i+1][j+1] = (dp[i][j]+dp[i][j+1]) % mod
        else:
            dp[i+1][j+1] = dp[i][j+1] % mod
print(dp[len(S)][8])
