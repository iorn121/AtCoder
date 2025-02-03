H,W = map(int,input().split())
S = [input() for _ in range(H)]

left=W
right=-1
top=H
bottom=-1
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            left=min(left,j)
            right=max(right,j)
            top=min(top,i)
            bottom=max(bottom,i)

flg = True
for i in range(top,bottom+1):
    for j in range(left,right+1):
        if S[i][j]==".":
            flg=False
            break
    if not flg:
        break

print("Yes" if flg else "No")