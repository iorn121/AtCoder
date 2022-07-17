N,X,Y= map(int, input().split())
if N==1: 
    exit(print(0))



def f(r,b):
    b+=r*X
    r+=b
    b*=Y
    return r,b

r,b=1,0
for i in range(N-1):
    r,b=f(r,b)
    # print(r,b)
print(b)