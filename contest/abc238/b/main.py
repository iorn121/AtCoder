N = int(input())
A = list(map(int, input().split()))

newA = [0]*(N+2)
cnt = 0
for i in range(N):
    cnt += A[i]
    if cnt >= 360:
        cnt -= 360
    newA[i+1] = cnt
newA[N+1] = 360
newA.sort()
ans = 0
for i in range(N+1):
    tmp = newA[i+1]-newA[i]
    ans = max(ans, tmp)
print(ans)
