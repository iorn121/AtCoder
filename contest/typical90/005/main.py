# https://drken1215.hatenablog.com/entry/2021/10/08/231200
MOD = 10**9+7
LOG = 62
N, B, K = map(int, input().split())
C = list(map(int, input().split()))


def mul(dpi, dpj, tj):
    res = [0]*B
    for p in range(B):
        for q in range(B):
            res[(p*tj+q) % B] += dpi[p]*dpj[q]
            res[(p*tj+q) % B] %= MOD
    return res


ten = [10]*LOG
for i in range(1, LOG):
    ten[i] = (ten[i-1]**2) % B

doubling = [[0]*B for _ in range(LOG)]

for k in range(K):
    doubling[0][C[k] % B] += 1

for i in range(1, LOG):
    doubling[i] = mul(doubling[i-1], doubling[i-1], ten[i-1])

res = [0]*B
res[0] = 1
for i in range(LOG):
    if (N >> i) & 1:
        res = mul(res, doubling[i], ten[i])
print(res[0])
