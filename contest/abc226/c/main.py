from collections import deque

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]
que = deque([N-1])
ans = 0
seen = [False]*N
while que:
    x = que.pop()
    now = L[x]
    ans += now[0]
    for other in now[2:]:
        if not seen[other-1]:
            seen[other-1] = True
            que.append(other-1)

print(ans)
