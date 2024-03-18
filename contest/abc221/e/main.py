N=int(input())
A=list(map(int,input().split()))

# 座標圧縮
X=set()
for a in A:
    X.add(a)
X=sorted(list(X))
M=len(X)
X2={X[i]:i for i in range(M)}
A2=[X2[a] for a in A]

mod=998244353
mod2=pow(2,mod-2,mod)

# fenwick tree
class FenwickTree:
    def __init__(self,n):
        self.n=n
        self.data=[0]*(n+1)
    def add(self,i,x):
        i+=1
        while i<=self.n:
            self.data[i]+=x
            self.data[i]%=mod
            i+=i&-i
    def sum(self,i):
        res=0
        i+=1
        while i>0:
            res+=self.data[i]
            res%=mod
            i-=i&-i
        return res

bit=FenwickTree(M)
ans=0
for i,a in enumerate(A2):
    ans+=bit.sum(a)*pow(2,i,mod)
    ans%=mod
    bit.add(a,pow(mod2,i+1,mod))

print(ans)