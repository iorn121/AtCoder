N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
s = set()

for b in B:
    s.add(A[0] ^ b)

ans = []
for x in s:
    C = [x ^ b for b in B]
    C.sort()
    if A == C:
        ans.append(x)
ans.sort()
print(len(ans))
for x in ans:
    print(x)
