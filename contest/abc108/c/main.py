N, K = map(int, input().split())
ans = pow(N//K, 3)

if K % 2 == 0:
    ans += pow((N+K//2)//K, 3)
print(ans)
