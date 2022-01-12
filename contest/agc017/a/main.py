N, P = map(int, input().split())
A = list(map(int, input().split()))
odd_bag = 0
even_bag = 0
ans = 0


def combination(n, r):
    result = 1
    if r > n//2:
        r = n-r
    for i in range(r):
        result = result*(n-i)//(i+1)
    return result


for a in A:
    if a % 2 == 0:
        even_bag += 1
    else:
        odd_bag += 1


if P == 0:
    for i in range(0, odd_bag+1, 2):
        ans += combination(odd_bag, i)
    ans *= 2**even_bag
    print(ans)
else:
    for i in range(1, odd_bag+1, 2):
        ans += combination(odd_bag, i)
    ans *= 2**even_bag
    print(ans)
