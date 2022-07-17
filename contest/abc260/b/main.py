N,X,Y,Z = map(int, input().split())
A= list(map(int, input().split()))
B= list(map(int, input().split()))
if X+Y+Z>=N:
    for i in range(N):
        print(i+1)
    exit()

check=[False]*N
nA=[(A[i],i) for i in range(N)]
nA.sort(key=lambda x:(-x[0],x[1]))
for i in range(X):
    # print(nA[i])
    check[nA[i][1]] = True

nB=[(B[i],i) for i in range(N) if not check[i]]
nB.sort(key=lambda x:(-x[0],x[1]))
# print(nB)
for i in range(Y):
    # print(nB[i])
    check[nB[i][1]] = True

nAB=[(A[i]+B[i],i) for i in range(N) if not check[i]]
nAB.sort(key=lambda x:(-x[0],x[1]))
# print(nAB)
for i in range(Z):
    # print(nAB[i])
    check[nAB[i][1]] =True

for i in range(N):
    if check[i]:
        print(i+1)

