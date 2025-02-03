N,Q = map(int, input().split())
pigeons= [i for i in range(N)]
nests = [1 for _ in range(N)]
ans = set()
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        P, H = q[1]-1, q[2]-1
        pre = pigeons[P]
        pigeons[P] = H
        nests[pre] -= 1
        if nests[pre] <= 1:
            ans.discard(pre)
        nests[H] += 1
        if nests[H] > 1:
            ans.add(H)
    elif q[0] == 2:
        print(len(ans))