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

N,K=map(int,input().split())
A=list(map(int,input().split()))
import itertools
import bisect
accum=list(itertools.accumulate(A))

ans=0
for i in range(N):
    left_limit=bisect.bisect_left(accum,K)
    ans+=N-left_limit
    K+=A[i]
print(ans)