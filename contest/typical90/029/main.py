W, N = map(int, input().split())


class SegTree:
    def __init__(self, N, unit_val, segfunc):
        self.X_unit = unit_val
        self.X_f = segfunc
        self.N = N
        self.X = [self.X_unit]*(2*N)

    def build(self, seq):
        for i, x in enumerate(seq, N):
            self.X[i] = x
        for i in range(N-1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)


class LazySegTree:
    def __init__(self, N, unit_val, segfunc):
        self.X_unit = unit_val
        self.X_f = segfunc
        self.N = N
        self.X = [self.X_unit]*(2*N)
        self.lazy = [None]*(2*N)

    def gindex(self, l, r):
        l += self.N
        r += self.N
        lm = (l//(l & -l)) >> 1
        rm = (r//(r & -r)) >> 1
        while l < r:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagate(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i << 1] = v
            self.lazy[i << 1 | 1] = v
            self.X[i << 1] = v
            self.X[i << 1 | 1] = v
            self.lazy[i] = None

    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagate(*ids)
        l += self.N
        r += self.N
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.X[l] = x
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = x
                self.X[r] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def build(self, seq):
        for i, x in enumerate(seq, N):
            self.X[i] = x
        for i in range(N-1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        *idx, = self.gindex(L, R)
        self.propagate(*idx)
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)


lst = LazySegTree(W, 0, max)
for i in range(N):
    l, r = map(int, input().split())
    cnt = lst.fold(l-1, r)
    lst.update(l-1, r, cnt+1)
    print(cnt+1)
