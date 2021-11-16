from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
a = []

for i in range(M):
    k = int(input())
    a.append(deque(list(map(int, input().split()))))

now = defaultdict(list)
queue = deque()

for i in range(M):
    x = a[i].popleft()
    now[x].append(i)

for x in now:
    if len(now[x]) == 2:
        queue.append(x)

while len(queue):
    x = queue.pop()
    for lx in now[x]:
        if len(a[lx]) != 0:
            nextx = a[lx].popleft()
            now[nextx].append(lx)
            if len(now[nextx]) == 2:
                queue.append(nextx)

for i in range(M):
    if len(a[i]) != 0:
        print("No")
        exit()
print("Yes")
