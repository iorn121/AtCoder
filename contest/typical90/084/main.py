import itertools
N=int(input())
S=list(input())

ans=N*(N-1)//2
for k,g in itertools.groupby(S):
    n=len(list(g))
    ans-=n*(n-1)//2
print(ans)