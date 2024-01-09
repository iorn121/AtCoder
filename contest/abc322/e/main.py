N, K, P = map(int, input().split())
mask = int("7" * K, 16)
mmm = int("8" * K, 16)
ppp = int(str(P) * K, 16)
minP = lambda x: x - ((((mmm + x - ppp) & mmm) * 7 >> 3) & (mmm + x - ppp))
inf = 10 ** 12
M = 1 << 4 * K - 1
L = [inf] * M
L[0] = 0
for _ in range(N):
    I = input().split()
    cost = int(I[0])
    s = int("".join(I[1:]), 16)
    x = mask + 1
    while x > 0:
        x = (x - 1) & mask
        y = minP(x + s)
        L[y] = min(L[y], L[x] + cost)
print(L[ppp] if L[ppp] < inf else -1)