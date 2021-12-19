import itertools
N, M = map(int, input().split())

AB = [[] for _ in range(N)]
CD = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    AB[A].append(B)
    AB[B].append(A)
for i in range(M):
    C, D = map(int, input().split())
    C -= 1
    D -= 1
    CD[C].append(D)
    CD[D].append(C)
flg = False
for x in itertools.permutations(range(N)):
    convert = [x[i] for i in range(N)]
    check = True
    for i in range(N):
        ab = AB[i]
        cd = CD[convert[i]]
        newcd = []
        for j in cd:
            newcd.append(convert.index(j))
        if set(ab) != set(newcd):
            check = False
    if check:
        flg = True


print("Yes" if flg else "No")
