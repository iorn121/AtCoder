N = int(input())
check = set()
for i in range(2, N):
    x = i*i
    if x > N:
        break
    while x <= N:
        check.add(x)
        x *= i

print(N-len(check))
