N,P,K= map(int, input().split())
A=[list(map(int, input().split())) for _ in range(N)]

def warshall_floyd(x):
    dist=[[x if m<0 else m for m in a] for a in A]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    count=0
    for i in range(N):
        for j in range(i):
            if dist[i][j]<=P:
                count+=1
    return count

def getMin(k):
    left=0
    right=P+1
    while left+1<right:
        mid = (left+right)//2
        if warshall_floyd(mid)<=k:
            right= mid
        else:
            left= mid
    return right

corner=warshall_floyd(P+1)

if corner==K:
    print("Infinity")
elif corner>K:
    print(0)
else:
    print(getMin(K-1)-getMin(K))