N=int(input())
points=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    ans=-1
    dist=-1
    for j in range(N):
        if i==j:
            continue
        d=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
        if d>dist:
            dist=d
            ans=j+1
    print(ans)