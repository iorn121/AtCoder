N = int(input())
S = [input() for _ in range(N)]

X = [0]*N
Y = [0]*N
Z = [0]*N
order = []
last = []

for i, s in enumerate(S):
    cnt = 0
    for c in s:
        if c.isdigit():
            cnt += X[i]*int(c)
            Y[i] += int(c)
        elif c == "X":
            X[i] += 1
    Z[i] = cnt
    if X[i] == 0:
        last.append((Y[i], i))
    else:
        order.append((Y[i]/X[i], i))

order.sort()
last.sort()
ans = sum(Z)
X_sum = 0
for o in order:
    _, i = o
    ans += X_sum*Y[i]
    X_sum += X[i]
for l in last:
    ans += X_sum*l[0]
print(ans)
