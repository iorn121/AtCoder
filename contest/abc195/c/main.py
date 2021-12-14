N = int(input())

cnt = 0
for i in range(6):
    if 1000**i <= N < 1000**(i+1):
        cnt = i
ans = 0
for i in range(cnt):
    ans += 1000**i*999*i
ans += (N-1000**cnt+1)*cnt
print(ans)
