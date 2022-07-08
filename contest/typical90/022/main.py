A, B, C = map(int, input().split())


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


g = gcd(A, B)
g = gcd(g, C)
ans = A//g+B//g+C//g-3
print(ans)
