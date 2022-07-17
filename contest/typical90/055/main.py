N,P,Q= map(int, input().split())
A= list(map(int, input().split()))

A=[a%P for a in A]

ans=0
from itertools import combinations
for i,j,k,l,m in combinations(A,5):
    if i%P*j%P*k%P*l%P*m%P==Q:
        ans+=1
print(ans)