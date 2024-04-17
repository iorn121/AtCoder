N=int(input())
A=list(map(int,input().split()))

class BIT:
    def __init__(self,n):
        self.n=n
        self.bit=[0]*(n+1)
    def add(self,i,w):
        i+=1
        while i<=self.n:
            self.bit[i]+=w
            i+=i&-i
    def sum(self,i):
        res=0
        i+=1
        while i:
            res+=self.bit[i]
            i-=i&-i
        return res

bit=BIT(N)
ans=0
for i,a in enumerate(A):
    ans+=i-bit.sum(a)
    bit.add(a,1)

for a in A:
    print(ans)
    # print(a,bit.sum(a)-1,N-bit.sum(a))
    ans-=bit.sum(a)-1
    ans+=N-bit.sum(a)
