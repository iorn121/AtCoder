S = input()

N = len(S)


def sum_num(x):
    x %= MOD
    return x*(x+1)//2


MOD = 998244353

ans = 0

for i in range(N-1):
    ans += sum_num(9*(10**i))
    ans %= MOD

ans += sum_num(int(S)-10**(N-1)+1)
ans %= MOD
print(ans)
