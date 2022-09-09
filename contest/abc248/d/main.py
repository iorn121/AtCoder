import bisect


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
M = max(A)
S = [[] for _ in range(N+1)]
for i in range(N):
    a = A[i]
    S[a].append(i)
# print(ruiseki)
Q = int(input())
for i in range(Q):
    L, R, X = map(int, input().split())
    L -= 1
    R -= 1
    Xlist = S[X]
    # print(Xlist)
    # print(bisect.bisect_right(Xlist, R))
    # print(bisect.bisect_left(Xlist, L))
    ans = bisect.bisect_right(Xlist, R)-bisect.bisect_left(Xlist, L)
    print(ans)
