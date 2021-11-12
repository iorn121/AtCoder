N, M = map(int, input().split())

total = 0
connctions = []
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    connctions.append([A, B, C])
    total += C

parent = [i for i in range(N)]
rank = [1]*N


def find_origin(u):
    while u != parent[u]:
        parent[u], u = parent[parent[u]], parent[u]
    return u


def union(u, v):
    root_u = find_origin(u)
    root_v = find_origin(v)

    if root_u == root_v:
        return False

    if rank[root_v] > rank[root_u]:
        root_u, root_v = root_v, root_u

    parent[root_v] = root_u
    rank[root_u] += rank[root_v]

    return True


connctions.sort(key=lambda x: x[2])
sm = 0

for u, v, val in connctions:
    if union(u, v):
        sm += val
    elif val < 0:
        sm += val

print(total-sm)
