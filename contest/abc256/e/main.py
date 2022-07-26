N= int(input())
X= list(map(int, input().split()))
C= list(map(int, input().split()))
G=[X[i]-1 for i in range(N)]
seen=[False]*N
ans=0
for i in range(N):
    if seen[i]:
        continue
    cur=i
    seen_local=set()
    ans_local=0
    while True:
        if seen[cur] and (cur not in seen_local):
            break
        if cur in seen_local:
            ans_local=C[cur]
            nxt=G[cur]
            while nxt != cur:
                ans_local=min(ans_local,C[nxt])
                nxt=G[nxt]
            break
        seen[cur]=True
        seen_local.add(cur)
        cur=G[cur]
    ans+=ans_local
print(ans)