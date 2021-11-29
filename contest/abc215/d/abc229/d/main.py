S = input()
K = int(input())

N = len(S)
ruiseki = [0]*(N+1)
for i in range(N):
    if S[i] == ".":
        ruiseki[i+1] = ruiseki[i]+1
    else:
        ruiseki[i+1] = ruiseki[i]

ans = 0
r = 0
for l in range(N):
    while r < N and ruiseki[r+1]-ruiseki[l] <= K:
        r += 1
    ans = max(ans, r-l)

print(ans)
