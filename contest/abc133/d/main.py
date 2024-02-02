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

N=int(input())
A=list(map(int,input().split()))

ans=[0]*N
cnt=0
for a in A:
    cnt=a*2-cnt
    # print(cnt)
ans[0]=cnt//2
for i,a in enumerate(A[:-1]):
    ans[i+1]=a*2-ans[i]
print(*ans)
