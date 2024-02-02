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

N,K = map(int, input().split())

import math

ans=[0]*K
MOD=10**9+7
red=N-K
for i in range(1,K+1):
    # print(math.comb(red+1,i))
    # print(math.comb(K-1,i-1))
    ans[i-1]=math.comb(red+1,i)%MOD*math.comb(K-1,i-1)%MOD
print(*ans,sep="\n")