S = input()
N = len(S)

ans = 0
check = 0
now = ''
for i in range(2, N):
    if S[i-2] == S[i-1] and S[i-1] != S[i] and S[i-1] != now:
        now = S[i-1]
        check += 1
    ans += check
    if S[i] == now:
        ans -= 1
    # print(check, now, ans)
print(ans)
