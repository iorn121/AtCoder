N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

wa = A+B-2
sa = A-B

for i in range(P-1, Q):
    ans = ""
    for j in range(R-1, S):
        if i+j == wa or i-j == sa:
            ans += "#"
        else:
            ans += "."
    print(ans)
