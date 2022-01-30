N = int(input())
S = input()

ans = [-1]*(N+1)
cnt = 0
ccnt = N
for i in range(N):
    if S[i] == 'R':
        ans[cnt] = i
        cnt += 1
    else:
        ans[ccnt] = i
        ccnt -= 1
ans[cnt] = N
print(*ans)
