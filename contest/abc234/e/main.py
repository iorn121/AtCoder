X = input()
N = len(X)
ans = int("1"*18)
for i in range(-9, 9, 1):
    if i == 0:
        continue
    for s in range(1, 10):
        candidate = s
        t = s
        while 0 <= t+i <= 9:
            t += i
            candidate = candidate*10 + t
            if candidate >= int(X):
                ans = min(ans, candidate)
for i in range(1, 10):
    tmp = i
    for l in range(1, 18):
        if tmp >= int(X):
            ans = min(ans, tmp)
        tmp *= 10
        tmp += i
print(ans)
