import heapq
from collections import defaultdict
N,K = map(int, input().split())
A= list(map(int, input().split()))
D=[[] for _ in range(K)]
for i,a in enumerate(A):
    D[i%K].append(a)
newA=A[::1]
newA.sort()
for i in range(K):
    D[i].sort()

reA=[0]*N
for i in range(K):
    for j,x in enumerate(D[i]):
        reA[i+j*K]=x

if newA==reA:
    print("Yes")
else:
    print("No")