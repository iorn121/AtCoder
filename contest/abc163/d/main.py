N,K=map(int,input().split())
ans=0
mod=10**9+7
for i in range(K,N+2):
  ans+=i*(N-i+1)+1
  ans%=mod
print(ans%mod)
