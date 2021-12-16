import math
N = int(input())
A = list(map(int, input().split()))
left_ruiseki = [A[0]]
right_ruiseki = [A[N-1]]

left_now = A[0]
right_now = A[N-1]
for i in range(N-1):
    left_now = math.gcd(left_now, A[i+1])
    right_now = math.gcd(right_now, A[N-2-i])
    left_ruiseki.append(left_now)
    right_ruiseki.append(right_now)
right_ruiseki.reverse()

ans = 0
for i in range(N):
    if 0 < i < N-1:
        tmp = math.gcd(left_ruiseki[i-1], right_ruiseki[i+1])
        ans = max(ans, tmp)
    elif i == 0:
        ans = max(ans, right_ruiseki[i+1])
    else:
        ans = max(ans, left_ruiseki[i-1])
print(ans)
