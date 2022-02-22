N = int(input())
for i in range(N):
    L, R = map(int, input().split())
    m = min(10**9, R)
    M = max(0, L)
    print(max(0, (M-m+1)//2))
