N,C= map(int, input().split())
all0=0
all1=2**30-1
for i in range(N):
    T,A=map(int, input().split())
    if T==1:
        all0&=A
        all1&=A
    elif T==2:
        all0|=A
        all1|=A
    else:
        all0^=A
        all1^=A
    C=(C&all1)|(~C&all0)
    print(C)
