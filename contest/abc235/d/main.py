from collections import defaultdict
A, N = map(int, input().split())

INF = 10**18


d = defaultdict(int)
d[1] = 0
t = 1
cnt = 0
while t < 10**6:
    t *= A
    cnt += 1
    if t < 10:
        d[t] = 0+cnt
    elif t % 10 != 0:
        d[t] = 0+cnt
        tt = str(t)
        for i in range(1, len(tt)):
            tt = tt[-1]+tt[:-1]
            d[int(tt)] = i+cnt
    else:
        d[t] = 0+cnt


def check(s, x):
    if d[s]:
        return d[s]+x
    else:
        if s % 10 == 0:
            return check(s//A, x+1) if s % A == 0 else None
        now = INF
        if s % A == 0:
            aa = check(s//A, x+1)
            if aa is not None:
                now = aa
        s = str(s)
        for i in range(1, len(s)):
            s = s[1:]+s[0]
            ss = int(s)
            if ss % A == 0:
                if a := check(ss//A, x+i+1) is not None:
                    now = min(now, a)
        return now if now != INF else None


ans = check(N, 0)

print(ans if ans != None else -1)
