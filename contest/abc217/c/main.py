N = int(input())

P = list(map(int, input().split()))

ans = [-1]*N

for i in range(N):
    ans[P[i]-1] = i+1

print(*ans)
