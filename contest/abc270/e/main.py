def print_func_info(func):
    def wrapper(*args, **kwargs):
        print(f"executing {func}")
        for arg in args:
            print(f":param {type(arg)} {arg}")
        results = func(*args, **kwargs)
        for result in results:
            print(f":return: {result}")
        return results
    return wrapper


N, K = map(int, input().split())
A = list(map(int, input().split()))
m = -1
M = 10**12+1
while m+1 < M:
    mid = (m+M)//2
    cnt = 0
    for i in range(N):
        cnt += min(A[i], mid)
    if cnt > K:
        M = mid
    else:
        m = mid
ans = A[:]

for i in range(N):
    K -= min(m, A[i])
for i in range(N):
    ans[i] = max(0, A[i]-m)
    if K > 0 and ans[i] > 0:
        ans[i] -= 1
        K -= 1

print(*ans)
