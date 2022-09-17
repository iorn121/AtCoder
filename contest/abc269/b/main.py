S=[input() for _ in range(10)]

sx,sy,gx,gy=11,11,-1,-1
for i in range(10):
    for j in range(10):
        if S[i][j]=="#":
            sx=min(sx,j+1)
            sy=min(sy,i+1)
            gx=max(gx,j+1)
            gy=max(gy,i+1)

print(sy,gy)
print(sx,gx)