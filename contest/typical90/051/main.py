from bisect import bisect_left, bisect_right
N, K, P = map(int, input().split())
A = list(map(int, input().split()))
leftA = A[:N//2]
rightA = A[N//2:]


# def print_func_info(func):
#     def wrapper(*args, **kwargs):
#         print(f"executing {func}")
#         for arg in args:
#             print(f":param {type(arg)} {arg}")
#         results = func(*args, **kwargs)
#         for result in results:
#             print(f":return: {result}")
#         return results
#     return wrapper


class Product_list:
    def __init__(self, l):
        self.length = len(l)
        self._list = l
        self._num_list = [[] for _ in range(self.length+1)]

    def count(self):
        for i in range(1 << self.length):
            cnt = 0
            tmp = 0
            for j in range(self.length):
                if (i >> j) & 1:
                    cnt += 1
                    tmp += self._list[j]
            self._num_list[cnt].append(tmp)
        for i in range(self.length):
            self._num_list[i].sort()
        return self._num_list


l = Product_list(leftA)
r = Product_list(rightA)
l_list = l.count()
r_list = r.count()
ans = 0
for i in range(l.length+1):
    if i > K:
        continue
    if i+r.length < K:
        continue
    for x in l_list[i]:
        rest = P-x
        if rest < 0:
            continue
        y = bisect_right(r_list[K-i], rest)
        ans += y
print(ans)
