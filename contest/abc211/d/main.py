N, M = map(int, input().split())
roads = [[]for i in range(N)]
mod = 10**9+7

for i in range(M):
    A, B = map(int, input().split())
    roads[A-1].append(B-1)
    roads[B-1].append(A-1)

que = [0]

cnt = [-1]*N
cnt[0] = 0
ans = [0]*N
ans[0] = 1
for now in que:
    # print(now, "start")
    for nex in roads[now]:
        if cnt[nex] == -1:
            que.append(nex)
            cnt[nex] = cnt[now]+1
            ans[nex] = ans[now]
        elif cnt[nex] == cnt[now]+1:
            ans[nex] += ans[now]
            ans[nex] %= mod
        # print(nex, cnt[nex], ans[nex])

print(ans[N-1])
