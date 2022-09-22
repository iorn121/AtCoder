

MOD = 998244353


def alph_to_num(s):
    return ord(s)-ord('A')


T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    ans = 0
    for i in range((N+1)//2):
        ans *= 26
        ans += alph_to_num(S[i])
        ans %= MOD
    if N % 2 == 0 and S[:N//2]+S[:N//2][::-1] <= S:
        ans += 1
    if N % 2 == 1 and S[:N//2+1]+S[:N//2][::-1] <= S:
        ans += 1
    ans %= MOD
    print(ans)
