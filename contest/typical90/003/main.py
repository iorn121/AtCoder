import queue
N = int(input())
road = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    road[A].append(B)
    road[B].append(A)


def farthest(start):
    distance = [-1]*N
    q = queue.Queue()
    distance[start] = 0
    q.put(start)
    while not q.empty():
        now = q.get()
        for nex in road[now]:
            if distance[nex] == -1:
                distance[nex] = distance[now]+1
                q.put(nex)
    max_val = max(distance)
    max_town = distance.index(max_val)
    return (max_val, max_town)


m1v, m1t = farthest(0)
m2v, m2t = farthest(m1t)
print(m2v+1)
