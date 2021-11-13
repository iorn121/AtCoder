import math
N = int(input())


ans = 0


for i in range(1, N+1):
    if i**3 > N:
        break
    for j in range(i, N+1):
        if i*j*j > N:
            break
        ans += N//(i*j)-(j-1)

print(ans)
