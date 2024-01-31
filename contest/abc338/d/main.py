from atcoder.lazysegtree import LazySegTree
N,M=[int(x) for x in input().split()]
X=[int(x)-1 for x in input().split()]
mincost=sum(min((X[i]-X[i-1])%N,(X[i-1]-X[i])%N) for i in range(1,M))
def op(x,y):
  return x+y

e=0

def mapping(x,y):
  return x+y

def composition(x,y):
  return x+y

id_=0

lst=LazySegTree(op, e, mapping, composition, id_, N)
for i in range(1,M):
  l,r=min(X[i],X[i-1]),max(X[i],X[i-1])
  diff=max((r-l)%N,(l-r)%N)-min((r-l)%N,(l-r)%N)
  if diff==0:
    continue
  if r-l<N-r+l:
    lst.apply(l,r,diff)
  else:
    lst.apply(0,l,diff)
    lst.apply(r,N,diff)

ans=lst.get(0)
for i in range(1,N):
  ans=min(ans,lst.get(i))
print(mincost+ans)