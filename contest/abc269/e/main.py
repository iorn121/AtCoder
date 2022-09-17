N= int(input())


A,B,C,D=0,N+1,0,N+1
while A+1<B:
    mid = (A+B)//2
    print("?",1,mid,1,N)
    ans= int(input())
    if ans==mid:
        A=mid
    else:
        B=mid
while C+1<D:
    mid = (C+D)//2
    print("?",1,N,1,mid)
    ans= int(input())
    if ans==mid:
        C=mid
    else:
        D=mid
print("!",B,D)