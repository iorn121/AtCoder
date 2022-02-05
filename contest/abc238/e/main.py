N, Q = map(int, input().split())
temoti = []*N
for i in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    temoti[l].append(r)
now = 0
