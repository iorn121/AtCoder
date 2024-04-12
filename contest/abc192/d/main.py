X=int(input())
M=int(input())

def f(n):
    x=X
    ans=0
    i=0
    while x:
        d=x%10
        ans+=d*(n**i)
        if ans>M:
            return False
        x//=10
        i+=1
    # print(n,ans,"True")
    return True

if len(str(X))==1 and X<=M:
    print(1)
    exit()

limit=10**20
max_d=max(map(int,list(str(X))))
left=max_d
right=limit+1
while right-left>1:
    # print(left,right)
    mid=(left+right)//2
    if f(mid):
        left=mid
    else:
        right=mid

print(left-max_d) if left>=max_d else print(0)