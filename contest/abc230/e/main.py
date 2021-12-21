import math
N = int(input())
K = math.floor(math.sqrt(N))

ans = 0
for i in range(1, K+1):
    ans += (N//i-N//(i+1))*i

for i in range(1, N//(K+1)+1):
    ans += N//i
print(ans)
