H,W=map(int,input().split())

S=[input() for _ in range(H)]

N=H*W
edge=[[] for _ in range(N)]
for i in range(H):
    for j in range(W):
        cp=W*i+j
        for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            nx,ny=i+dx,j+dy
            if 0<=nx<H and 0<=ny<W and S[nx][ny]=="#":
                nv=W*nx+ny
                edge[cp].append(nv)

parent=[-1]*N
lowlink=[-1]*N
v_ord=[-1]*N
child=[0]*N

tree_edge=[[] for _ in range(N)]
def calc_lowlink(start):
    stack=[(start,-1)]
    nxt_ord=0
    visited=[]
    while stack:
        v,pv=stack.pop()
        if v<0:
            v=~v
            lowlink[v]=v_ord[v]
            for nv in edge[v]:
                if nv==parent[v]:
                    continue
                if v_ord[nv]>v_ord[v]:
                    lowlink[v]=min(lowlink[v],lowlink[nv],v_ord[nv])
                else:
                    lowlink[v]=min(lowlink[v],v_ord[nv])
            continue

        if v_ord[v]!=-1:
            continue
        if pv!=-1:
            child[pv]+=1
            parent[v]=pv
            tree_edge[pv].append(v)
        v_ord[v]=nxt_ord
        visited.append(v)
        nxt_ord+=1
        stack.append((~v,-1))
        for nv in edge[v]:
            stack.append((nv,v))
    
    res=0
    for v in visited:
        if v==start:
            if child[v]:
                res+=child[v]-1
        else:
            for nv in tree_edge[v]:
                if nv==parent[v]:
                    continue
                if lowlink[nv]>=v_ord[v]:
                    res+=1
    
    return res,len(visited)

green=0
d=0
c=0
for i in range(H):
    for j in range(W):
        if S[i][j]=='.':
            continue
        green+=1
        v=W*i+j
        if v_ord[v]!=-1:
            continue
        a,b=calc_lowlink(v)
        if b==1:
            d-=1
        else:
            d+=a
        c+=1
        
Mod=998244353
res=d
res*=pow(green,-1,Mod)
res+=c
res%=Mod
print(res)