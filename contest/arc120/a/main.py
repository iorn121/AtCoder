N = int(input())
A = list(map(int, input().split()))
M = 0
sm = 0
cnt = 0
for i in range(N):
    M = max(M, A[i])
    sm += A[i]
    cnt += sm
    print(cnt+M*(i+1))
