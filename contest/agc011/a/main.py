N, C, K = map(int, input().split())

T = [int(input()) for _ in range(N)]
T.sort()
ans = 1
cnt = 0
prev = T[0]+K
for i in range(N):
    if cnt < C and T[i] <= prev:
        cnt += 1
    else:
        cnt = 1
        ans += 1
        prev = T[i]+K

print(ans)
