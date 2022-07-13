N,Q= map(int, input().split())
A=list(map(int, input().split()))
cnt=0
for _ in range(Q):
    T,X,Y=map(int, input().split())
    if T==1:
        X-=1
        Y-=1
        x=X-cnt if X-cnt>=0 else (X-cnt)%N
        y=Y-cnt if Y-cnt>=0 else (Y-cnt)%N
        A[x],A[y] = A[y], A[x]
    if T==2:
        cnt+=1
    if T==3:
        print(A[(X-1-cnt)%N])
    # print(A,cnt)