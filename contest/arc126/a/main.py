

def solve(n2, n3, n4):
    N1, N2, N3 = n2, n3, n4//2
    ans = 0

    combo = [(0, 1, 1), (2, 0, 1), (1, 2, 0), (3, 1, 0), (5, 0, 0)]
    for a, b, c in combo:
        x = N1+N2+N3
        if a > 0:
            x = min(x, N1//a)
        if b > 0:
            x = min(x, N2//b)
        if c > 0:
            x = min(x, N3//c)
        ans += x
        N1 -= a*x
        N2 -= b*x
        N3 -= c*x

    print(ans)


N = int(input())
for i in range(N):
    A, B, C = map(int, input().split())
    solve(A, B, C)
