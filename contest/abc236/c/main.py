N, M = map(int, input().split())
S = input().split()
T = input().split()
ans = [False]*len(S)

now = 0
for i, s in enumerate(S):
    if s == T[now]:
        ans[i] = True
        now += 1

for a in ans:
    print('Yes' if a else 'No')
