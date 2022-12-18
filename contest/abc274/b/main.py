H,W = map(int, input().split())
S=[input() for _ in range(H)]

ans=[0]*W
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            ans[j]+=1

print(*ans)