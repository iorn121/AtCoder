N = int(input())
S = input()


def combination(x):
    return x*(x-1)//2


cnt = 1
ans = 0
for i in range(1, N):
    if S[i-1] == S[i]:
        cnt += 1
    else:
        ans += combination(cnt)
        cnt = 1
ans += combination(cnt)
print(ans)
