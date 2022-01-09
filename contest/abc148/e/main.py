N = int(input())

if N % 2 == 1:
    print(0)
else:
    ans = N//10
    N //= 10
    i = 1
    while N // (5**i) > 0:
        ans += N//(5**i)
        i += 1
    print(ans)
