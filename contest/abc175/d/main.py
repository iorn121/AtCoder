N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

P = [p-1 for p in P]  # 0-indexedにする

INF = 10**18
ans = -INF

for i in range(N):
    v = i
    cycle_sum = 0
    cycle_cnt = 0

    while True:
        cycle_cnt += 1
        cycle_sum += C[v]
        v = P[v]
        if v == i:
            break

    path = 0
    cnt = 0

    while True:
        cnt += 1
        path += C[v]

        if cnt > K:
            break

        num = (K - cnt) // cycle_cnt
        score = path + max(0, cycle_sum) * num
        ans = max(ans, score)

        v = P[v]
        if v == i:
            break

print(ans)