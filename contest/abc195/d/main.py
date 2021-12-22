N, M, Q = map(int, input().split())
WV = []
for _ in range(N):
    W, V = map(int, input().split())
    WV.append((W, V))
WV.sort(key=lambda x: -x[1])
X = list(map(int, input().split()))
LR = []
for i in range(Q):
    L, R = map(int, input().split())
    LR.append((L, R))


def f(box: list) -> int:
    result = 0
    used = [False]*len(box)

    for w, v in WV:
        for i, capa in enumerate(box):
            if w <= capa and used[i] == False:
                result += v
                used[i] = True
                break

    return result


for l, r in LR:
    box = X[:l-1]+X[r:]
    box.sort()
    print(f(box))
