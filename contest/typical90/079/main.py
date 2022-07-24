H,W= map(int, input().split())
A=[list(map(int, input().split())) for _ in range(H)]
B=[list(map(int, input().split())) for _ in range(H)]

sabun=[[A[i][j]-B[i][j] for j in range(W)] for i in range(H)]
play=[[0]*(W-1) for _ in range(H-1)]
ans=0
for i in range(H-1):
    for j in range(W-1):
        if i==0 and j==0:
            play[i][j]=sabun[i][j]
        elif i==0:
            play[i][j]=sabun[i][j]-play[i][j-1]
        elif j==0:
            play[i][j]=sabun[i][j]-play[i-1][j]
        else:
            play[i][j]=sabun[i][j]-play[i-1][j-1]-play[i-1][j]-play[i][j-1]
        ans+=abs(play[i][j])
cnt=0
for i in range(H):
    for j in range(W):
        sabun[i][j]*=(-1)**((i+j)%2)
        cnt+=sabun[i][j]
if cnt==0:
    print("Yes")
    print(ans)
else:
    print("No")
