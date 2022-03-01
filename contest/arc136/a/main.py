N = int(input())
S = input()


def solution(n):
    s = 'A'*(n//2)
    if n % 2 == 1:
        s += 'B'
    return s


ans = ''
cnt = []
tmp = 0
for s in S:
    if s == 'A':
        tmp += 2
    elif s == 'B':
        tmp += 1
    else:
        if tmp > 0:
            ans += solution(tmp)
            tmp = 0
        ans += 'C'
ans += solution(tmp)
print(ans)
