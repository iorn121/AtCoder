N = int(input())
deg = [0]*N
G = [[] for _ in range(N)]

for _ in range(N):
    U, V = map(lambda x: int(x)-1, input().split())
    G[U].append(V)
    G[V].append(U)
    deg[U] += 1
    deg[V] += 1

Q = int(input())

visited = [-1]*(N)
q = [i for i, v in enumerate(deg) if v == 1]

while len(q):
    nq = []
    for cur in q:
        for nex in G[cur]:
            if visited[nex] == -1:
                visited[cur] = nex
                deg[nex] -= 1
                if deg[nex] == 1:
                    nq.append(nex)
    q = nq

# print(visited)


def find_root(x):
    if visited[x] == x:
        return x
    if visited[x] == -1:
        visited[x] = x
        return x
    visited[x] = find_root(visited[x])
    return visited[x]


for i in range(N):
    find_root(i)

# print(visited)

for _ in range(Q):
    X, Y = map(lambda x: int(x)-1, input().split())
    print("Yes" if visited[X] == visited[Y] else "No")
