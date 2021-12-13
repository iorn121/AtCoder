S = input()
N = int(S)
ans = 0
for i in range(1, 10**6):
    s = str(i)*2
    n = int(s)
    if N >= n:
        ans += 1
print(ans)
