H, W = map(int, input().split())
S = []
MOD = 998244353
for i in range(H):
    S.append(input())
ans = 1
check = [[0, 0, 0]for i in range(H+W)]
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            check[i+j][0] += 1
        elif S[i][j] == "R":
            check[i+j][1] += 1
        else:
            check[i+j][2] += 1
for i in range(H+W-1):
    if check[i][1] and check[i][2]:
        ans *= 0
    elif check[i][1] == 0 and check[i][2] == 0:
        ans *= 2
    ans %= MOD

print(ans)
