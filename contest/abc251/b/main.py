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


N, W = map(int, input().split())
A = list(map(int, input().split()))

s = set()
for a in A:
    s.add(a)

for i in range(N-1):
    for j in range(i+1, N):
        s.add(A[i]+A[j])

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            s.add(A[i]+A[j]+A[k])

ns = list(s)
ns.sort()
ans = bisect.bisect_right(ns, W)
# print(ns)
print(ans)
