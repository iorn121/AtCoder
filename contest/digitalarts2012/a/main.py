import re
S = input().split()
N = int(input())
T = [input().replace('*', r'[a-z]') for _ in range(N)]
ans = S[:]

for i, s in enumerate(S):
    for t in T:
        if re.fullmatch(t, s):
            ans[i] = '*'*len(s)

print(*ans)
