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


N, K = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = 0
for i in range(1 << N):
    k = 0
    d = defaultdict(int)
    for j in range(N):
        if (i >> j) & 1:
            k += 1
            for s in S[j]:
                d[s] += 1
            # print(j)
    # print(d)
    cnt = 0
    for x in d.values():
        # print(x)
        if x == K:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
