from itertools import permutations

S = list(input())
n = len(S)
ans = 0
for i in permutations(S):
    for j in range(1, (n+1)//2):
        x = int("".join(i[:j]))
        y = int("".join(i[j:]))
        ans = max(ans, x*y)

print(ans)
