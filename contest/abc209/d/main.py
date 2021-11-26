import queue
N, Q = map(int, input().split())
road = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    road[a].append(b)
    road[b].append(a)

color = [-1]*(N+1)

color[1] = 0

que = queue.Queue()
que.put(1)

while not que.empty():
    now = que.get()
    for i in road[now]:
        if color[i] == -1:
            color[i] = 1-color[now]
            que.put(i)

for _ in range(Q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
