from collections import defaultdict


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


N = int(input())
A = list(map(int, input().split()))
dp1 = [[10**15]*2 for _ in range(N+1)]
dp2 = [[10**15]*2 for _ in range(N+1)]
dp1[1][0] = 0
dp2[1][1] = A[0]
for i in range(2, N+1):
    dp1[i][0] = dp1[i-1][1]
    dp1[i][1] = min(dp1[i-1])+A[i-1]
    dp2[i][0] = dp2[i-1][1]
    dp2[i][1] = min(dp2[i-1])+A[i-1]
ans = min(min(dp2[N]), dp1[N][1])
print(ans)
