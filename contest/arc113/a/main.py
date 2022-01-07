K = int(input())

ans = 0

for a in range(1, K+1):
    if a**3 > K:
        break
    for b in range(a, K+1):
        if a*b*b > K:
            break
        if a == b:
            ans += 1
            ans += 3*(K//(a*b)-b)
        else:
            ans += 3
            ans += 6*(K//(a*b)-b)

print(ans)
