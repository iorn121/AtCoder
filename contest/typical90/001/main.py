from re import I


N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)


def check(x):
    tmp = 0
    cnt = 0
    flg = True
    for a in A:
        if a-tmp >= x:
            tmp = a
            cnt += 1
    if cnt < K+1:
        flg = False
    return flg


l = 1
r = 10**9
while l+1 < r:
    mid = (l+r)//2
    if check(mid):
        l = mid
    else:
        r = mid
    # print(f"l-r: {l}-{r}")

print(l)
