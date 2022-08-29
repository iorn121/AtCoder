N,Q= map(int, input().split())
A=list(map(int, input().split()))
A.sort()
ruiseki=[0]
for i in range(N):
    ruiseki.append(ruiseki[-1]+A[i])
import bisect
for i in range(Q):
    X=int(input())
    p=bisect.bisect_right(A, X)
    ans=X*p-ruiseki[p]+ruiseki[N]-ruiseki[p]-X*(N-p)
    print(ans)