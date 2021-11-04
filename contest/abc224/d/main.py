from collections import deque


def to_string(value):
    str = "".join(value)
    return str


M = int(input())

root = [[] for i in range(9)]

for i in range(M):
    v1, v2 = (x-1 for x in map(int, input().split()))
    root[v1].append(v2)
    root[v2].append(v1)


positions = [x-1 for x in map(int, input().split())]
start_status = ["9"]*9
for i in range(len(positions)):
    start_status[positions[i]] = str(i+1)

goal = [str(x+1) for x in range(9)]
seen = set()
que = deque()
que.append((start_status, 0))
ans = -1

while que:
    status, d = que.popleft()
    if status == goal:
        ans = d
        break

    nonLeft = status.index("9")
    for v in root[nonLeft]:
        n_status = status[:]
        n_status[v], n_status[nonLeft] = n_status[nonLeft], n_status[v]
        n_str = to_string(n_status)
        if n_str not in seen:
            seen.add(n_str)
            que.append((n_status, d+1))

print(ans)
