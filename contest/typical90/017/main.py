N, M = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(M)]

LR.sort(key=lambda x: (x[1], -x[0]))


class BIT:
    def __init__(self, N):
        self.size = N
        self.bit = [0]*(N+1)

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= -i & i
        return res

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += -i & i


ans = 0
bit_l = BIT(N)
bit_r = BIT(N)
for i, (l, r) in enumerate(LR):
    ans += bit_l.sum(l-1)-bit_r.sum(l)
    bit_l.add(l, 1)
    bit_r.add(r, 1)
    # print(f"i: {i}, ans: {ans}")
print(ans)
