N, B = map(int, input().split())

if N < B:
    exit(print(0))


def f(m):
    num = 1
    for s in str(m):
        num *= int(s)
    return num


prime = [2, 3, 5, 7]
fm_list = set([0])


def dfs(fm, p):
    if fm+B > N:
        return None
    fm_list.add(fm)
    for i in range(p, 4):
        dfs(fm*prime[i], i)


dfs(1, 0)

ans = 0
for fm in fm_list:
    if f(fm+B) == fm:
        ans += 1

print(ans)
