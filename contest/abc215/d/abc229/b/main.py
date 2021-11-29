A, B = input().split()

A = A[::-1]
B = B[::-1]
ans = "Easy"
for i in range(min(len(A), len(B))):
    if int(A[i])+int(B[i]) > 9:
        ans = "Hard"
print(ans)
