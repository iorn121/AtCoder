import math
A, B = map(int, input().split())

gcd = math.gcd(A, B)


def factorization(x):
    result = []
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            result.append((i, cnt))
    if x != 1:
        result.append((x, 1))
    return result


fact = factorization(gcd)

print(len(fact)+1)
