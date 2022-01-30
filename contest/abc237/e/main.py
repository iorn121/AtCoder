from collections import deque
N, M = map(int, input().split())
H = list(map(int, input().split()))


def check(x, y):
    if x < y:
        return 2*(x-y)
    else:
        return x-y


root = [[] for i in range(N)]
for i in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    root[U].append(V)
    root[V].append(U)
q = deque()
q.append(0)
cnt = [-10**15]*N
cnt[0] = 0
visit = [False]*N
visit[0] = True
visited = ['0' for i in range(N)]
while q:
    now = q.pop()
    tanoshisa = cnt[now]
    for ikisaki in root[now]:
        n = tanoshisa+check(H[now], H[ikisaki])-cnt[ikisaki]
        if not visit[ikisaki]:
            visit[ikisaki] = True
            q.append(ikisaki)
            cnt[ikisaki] = tanoshisa+check(H[now], H[ikisaki])
            visited[ikisaki] = visited[now]+'-'+str(ikisaki)

        elif n > 0:
            for i in range(N):
                if str(ikisaki) in visited[ikisaki]:
                    cnt[ikisaki] += n

print(max(cnt))
