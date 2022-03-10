A, B = map(int, input().split())
ans = []
if A > B:
    for i in range(A):
        ans.append(i+1)
    for i in range(B-1):
        ans.append(-(i+1))
    ans.append(-(A-B+1)*(A+B)//2)
else:
    for i in range(A-1):
        ans.append(i+1)
    for i in range(B):
        ans.append(-(i+1))
    ans.append((B-A+1)*(A+B)//2)
print(*ans)
