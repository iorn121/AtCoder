N,S= map(int, input().split())
AB=[tuple(map(int, input().split())) for _ in range(N)]

dp=[[False]*(S+1) for _ in range(N+1)]
dp[0][0]=True
for i in range(N):
    A,B=AB[i]
    for j in range(S+1):
        if j-A>=0:
            dp[i+1][j]|=dp[i][j-A]
        if j-B>=0:
            dp[i+1][j]|=dp[i][j-B]
# print(dp)
if not dp[N][S]:
    exit(print("Impossible"))

ans=""
T=S
for i in reversed(range(N)):
    A,B= AB[i]
    if T-A>=0:
        if dp[i][T-A]:
            T-=A
            ans+="A"
            continue
    if T-B>=0:
        if dp[i][T-B]:
            T-=B
            ans+="B"
print(ans[::-1])