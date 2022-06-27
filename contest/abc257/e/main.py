N = int(input())
C = list(map(int, input().split()))
c = min(C)
digit = N//c
rest = N % c
ans = []
for i in range(digit):
    for j in range(9, 0, -1):
        if C[j-1] <= rest+c:
            ans.append(str(j))
            rest -= C[j-1]-c
            break
print("".join(ans))
