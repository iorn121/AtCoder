N = int(input())
A = list(map(int, input().split()))
ans = 0
minus = 0
abs_min = 10**10
zero = False
for i in range(N):
    ans += abs(A[i])
    if A[i] < 0:
        minus += 1
    if A[i] == 0:
        zero = True
    abs_min = min(abs_min, abs(A[i]))

if zero or minus % 2 == 0:
    print(ans)
else:
    print(ans-abs_min*2)
