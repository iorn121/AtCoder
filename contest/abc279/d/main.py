A,B= map(float, input().split())


def df(t):
    ans=B*pow(t+1,1.5)-A/2
    return ans

def f(t):
    ans=t*B+pow(A*A/(t+1),1/2)
    return ans

left=-1
right=10**12
while right-left > 1:
    mid=(left+right)//2
    if df(mid)>=0:
        right=mid
    else:
        left= mid

if left==-1:
    print(A)
else:
    print(f'{min(f(left),f(right)):08f}')