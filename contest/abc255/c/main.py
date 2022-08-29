X,A,D,N= map(int, input().split())
if D<0:
    D=-D
    A=-A
    X=-X
m=A
M=A+D*(N-1)


if X<=m:
    print(m-X)
elif M<=X:
    print(X-M)
else:
    amari=(X-A)%D
    print(min(amari,D-amari))

