N = int(input())
ans = N
for b in range(0, 61):
    a = N//(2**b)
    c = N % (2**b)
    ans = min(ans, a+b+c)
print(ans)
