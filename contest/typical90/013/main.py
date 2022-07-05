import heapq


def dijkstra(s: int, graph: list):
    """Dijkstra

    Args:
        s (int): 始点
        graph (list): グラフのリスト
    """
    
    INF= 10**18
    dist = [INF]*N
    check=[False]*N
    dist[s]=0
    q=[(0,s)]
    while q:
        v=heapq.heappop(q)[1]
        if check[v]:
            continue
        check[v]=True
        for t,w in G[v]:
            if check[t]:
                continue
            if dist[t]<=dist[v]+w:
                continue
            dist[t]=dist[v]+w
            heapq.heappush(q,(dist[t],t))
    return dist



N,M = map(int, input().split())
G=[[] for _  in range(N)]
for i in range(M):
    A,B,C = map(int, input().split())
    G[A-1].append((B-1,C))
    G[B-1].append((A-1,C))

x=dijkstra(0,G)
y=dijkstra(N-1,G)

for i in range(N):
    print(y[i]+x[i])