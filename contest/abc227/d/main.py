
N, K = map(int, input().split())

A = list(map(int, input().split()))

ok = 0
ng = 10**24
while ok+1 < ng:
    md = (ok+ng)//2
    cnt = 0
    for i in range(N):
        cnt += min(A[i], md)
    if cnt >= K*md:
        ok = md
    else:
        ng = md

print(ok)
