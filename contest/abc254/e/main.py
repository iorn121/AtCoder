from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
Q = int(input())
for i in range(Q):
    # print("---", i+1)
    x, k = map(int, input().split())
    ans = x
    seen = set([x])
    q = deque()
    q.append(x)
    for _ in range(k):
        nq = deque()
        while q:
            y = q.pop()
            for z in G[y]:
                if z in seen:
                    continue
                ans += z
                seen.add(z)
                nq.append(z)
                # print(z)
        q = nq
    print(ans)
