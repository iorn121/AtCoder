N=int(input())
dist=[0]*(10**5*3)
k_max=0
for _ in range(N):
    L,R= map(int, input().split())
    dist[L]+=1
    dist[R]-=1
    k_max=max(k_max,R)
ans=[]
for i in range(1,k_max+1):
    dist[i]+=dist[i-1]
    if dist[i-1]==0 and dist[i]>0:
        ans.append(i)
    if dist[i]==0 and dist[i-1]>0:
        ans.append(i)
for i in range(0,len(ans),2):
    print(ans[i],ans[i+1])