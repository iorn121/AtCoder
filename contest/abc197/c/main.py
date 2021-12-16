N = int(input())
A = list(map(int, input().split()))
ans = 1 << 60
for i in range(1 << (N-1)):
    stock_or = A[0]
    tmp = 0
    for j in range(N-1):
        if (i >> j) & 1:
            tmp = tmp ^ stock_or
            stock_or = A[j+1]
        else:
            stock_or = stock_or | A[j+1]
    tmp = tmp ^ stock_or
    ans = min(ans, tmp)
print(ans)
