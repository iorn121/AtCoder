N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

_A = set(A)
_B = set(B)
total = len(_A & _B)
cnt = 0
for i in range(N):
    if A[i] == B[i]:
        cnt += 1
print(cnt)
print(total-cnt)
