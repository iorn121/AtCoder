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

UPPER = 2*10**5

cnt = [0]*(UPPER+1)
for i in range(N):
    cnt[A[i]] += 1

for i in range(UPPER):
    cnt[i+1] += cnt[i]

# cnt[i] = Aに含まれる i 以下の値の個数
# cnt[i] = |{ j | A[j]<=i }|

ans = 0
for j in range(N):
    ans += cnt[A[j]-1]*(N-cnt[A[j]])

print(ans)
