N,Q= map(int, input().split())
num=[]
for i in range(N):
    L=list(map(int, input().split()))
    num.append(L[1:])
for _ in range(Q):
    s,t = map(lambda x: int(x)-1, input().split())
    print(num[s][t])