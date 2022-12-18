N,Q= map(int, input().split())
num=N
ball=[i if i<=N else -1  for i in range(N+Q+1)]
convert={}
for _ in range(Q):
    ope=list(map(int, input().split()))
    if ope[0]==1:
        convert[ope[2]]=ope[1]
    elif ope[0]==2:
        num+=1
        ball[num]=ope[1]
    else:
        print(ball[ope[1]])