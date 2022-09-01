from collections import defaultdict
Q = int(input())


d = defaultdict(int)
m = 10**9
M = 0
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        d[q[1]] += 1
        m = min(m, q[1])
        M = max(M, q[1])
    elif q[0] == 2:
        if q[1] not in d.keys():
            continue
        delete = min(q[2], d[q[1]])
        d[q[1]] -= delete
        if d[q[1]] == 0:
            d.pop(q[1])
            if len(d) == 0:
                m = 10**9
                M = 0
            elif m == q[1]:
                m = min(d.keys())
            elif M == q[1]:
                M = max(d.keys())
    else:
        print(M-m)
    # print(d)
