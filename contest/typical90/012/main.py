import pprint
H, W = map(int, input().split())
G = [[False]*(W+2) for _ in range(H+2)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
P = [i for i in range(H*W+2)]


def find(x):
    if P[x] == x:
        return x
    else:
        return find(P[x])


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x > y:
        x, y = y, x
    P[y] = x


def flatten(y, x):
    return (y-1)*W+x


Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        G[q[1]][q[2]] = True
        for i in range(4):
            if G[q[1]+dy[i]][q[2]+dx[i]]:
                unite(flatten(q[1], q[2]), flatten(q[1]+dy[i], q[2]+dx[i]))
    else:
        if same(flatten(q[1], q[2]), flatten(q[3], q[4])) and G[q[1]][q[2]] and G[q[3]][q[4]]:
            print("Yes")
        else:
            print("No")

# pprint.pprint(G)
