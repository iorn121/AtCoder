N= int(input())
A=[input() for _ in range(N)]

flg=True
for i in range(N):
    for j in range(N):
        # ドローの時 - 以外なら×
        if A[i][j]=="-":
            continue
        
        if A[i][j]=="D" and A[j][i]=="D":
            continue
        
        if A[i][j]=="W" and A[j][i]=="L":
            continue
        
        if A[i][j]=="L" and A[j][i]=="W":
            continue
        
        flg=False

print("correct" if flg else "incorrect")
