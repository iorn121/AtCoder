import queue
N = int(input())
G = [[]for _ in range(N)]

for _ in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

point_color = [-1]*N
q = queue.Queue()
point_color[0] = 0
q.put(0)
while not q.empty():
    point = q.get()
    for next_point in G[point]:
        if point_color[next_point] > -1:
            continue
        next_color = 0 if point_color[point] == 1 else 1
        point_color[next_point] = next_color
        q.put(next_point)
# print(point_color)

point_group = [[] for _ in range(2)]
for i, x in enumerate(point_color):
    point_group[x].append(i+1)

if len(point_group[0]) >= N//2:
    print(*point_group[0][0:N//2])
else:
    print(*point_group[1][0:N//2])
