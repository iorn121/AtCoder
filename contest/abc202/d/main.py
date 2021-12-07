A, B, K = map(int, input().split())
ans = ""


def combination(n, r):
    result = 1
    for i in range(r):
        result = result*(n-i)//(i+1)
    return result


for i in range(A+B):
    total = A+B-1
    result = combination(total, B)
    if result >= K:
        ans += "a"
        A -= 1
    else:
        K -= result
        ans += "b"
        B -= 1

print(ans)
