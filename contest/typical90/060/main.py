N = int(input())
A = list(map(int, input().split()))


def LIS(num_list):
    INF = 10**10
    N_list = len(num_list)
    dp_min = [INF]*N_list
    P = []
    for i in range(N_list):
        ok = N_list
        ng = -1
        x = num_list[i]
        while ng+1 < ok:
            mid = (ng+ok)//2
            if dp_min[mid] >= x:
                ok = mid
            else:
                ng = mid
        dp_min[ok] = x
        P.append(ok+1)
    return P


l_left = LIS(A)
l_right = LIS(A[::-1])

ans =-1
for i in range(N):
    ans = max(ans, l_left[i]+l_right[N-i-1]-1)
print(ans)
