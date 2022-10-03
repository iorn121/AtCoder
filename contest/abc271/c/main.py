N= int(input())
A=list(map(int, input().split()))
A.sort()
As=list(set(A))

import bisect
if N==1:
    if A[0]==1:
        exit(print(1))
    else:
        exit(print(0))

l=-1
r=N+1
while l+1<r:
    mid= (l+r)//2
    index=bisect.bisect_right(As,mid)
    cnt=index+(N-index)//2
    # cnt=0
    # check=[False]*(10**9+1)
    # for a in A:
    #     if check[a]:
    #         continue
    #     if a<=mid:
    #         cnt+=1
    #         check[a]=True
    # cnt=cnt+(N-cnt)//2
    if cnt>=mid:
        l=mid
    else:
        r=mid

print(l)
