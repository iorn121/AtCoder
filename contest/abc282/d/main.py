N,M=map(int, input().split())
G=[[] for _ in range(N)]

for i in range(M):
    u,v=map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)

color=[-1]*N

even=set()
odd=set()
set_root=[set(i_l) for i,i_l in enumerate(G)]

import sys
sys.setrecursionlimit(10**6)

# 頂点 v を始点とした深さ優先探索
def dfs(v, G, color,visited):
    # G[v] に含まれる頂点 v2 について、
    visited.add(v)
    if color[v]==0:
        even.add(v)
    else:
        odd.add(v)
    for v2 in G[v]:
        # v2 がすでに探索済みならば、スキップする
        if color[v2] != -1:
            # 隣り合う頂点どうしが同じ色なら、答えは No
            if color[v2] == color[v]: 
                return False
            continue
        # そうでなければ、頂点 v2 の色を color[v] と逆にしたうえで
        # v2 始点で深さ優先探索を行う (関数を再帰させる)
        color[v2] = 1 - color[v]
        if not dfs(v2, G, color,visited): return False
    return True

used=[]
tans=0
for i in range(N):
    if color[i]!=-1:
        continue
    color[i]=1
    visited=set()
    flg=dfs(i,G,color,visited)
    if not flg: 
        exit(print(0))

    x=len(visited)
    used.append(x)
    ans=0
    for j in list(visited):
        if color[j]==0:
            ans+=len(odd-set_root[j])
        else:
            ans+=len(even-set_root[j])
    # print(ans)
    even=[]
    odd=[]
    tans+=ans//2
if len(used)>1:
    ans=0
    for u in used:
        ans+=u*(N-u)
    tans+=ans//2
print(tans)
