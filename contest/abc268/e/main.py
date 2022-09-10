N= int(input())
P=list(map(int, input().split()))
K=N//2
ans=0
cnt=[0]*N
tmp=0
half=0
for i,p in enumerate(P):
    sa=(i-p)%N
    cnt[sa]+=1
    if sa<K:
        half+=1
    ans+=min(sa,N-sa)
    tmp=ans
for i in range(N-1):
    tmp+=2*half-N
    ans=min(ans,tmp)
    l=half+cnt[N-i-1]-cnt[(N-i-K)%N]
    r=N-l
    print((N-i-1)%N,"plus",cnt[N-i-1])
    print((N-i-K)%N,"minus",cnt[(N-i-K)%N])
    print((l,r))
    l=half+cnt[N-i-1]-cnt[(N-i-K)%N]
    half=l
print(ans)
print(cnt)