N,Q=map(int,input().split())
A=list(map(int,input().split()))
ans=set(range(1,N+1))
for a in A:
    if a in ans:
        ans.remove(a)
    else:
        ans.add(a)
print(len(ans))