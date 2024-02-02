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

ans=[0]*(N+1)
for i in range(N,0,-1):
    if i*2>N:
        ans[i]=A[i-1]
    else:
        ans[i]=A[i-1]
        for j in range(i*2,N+1,i):
            ans[i]^=ans[j]
print(ans.count(1))
for i in range(1,N+1):
    if ans[i]==1:
        print(i,end=" ")