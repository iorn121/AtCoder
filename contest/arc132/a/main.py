N = int(input())
R = list(map(lambda x: int(x)-1, input().split()))
C = list(map(lambda x: int(x)-1, input().split()))
Q = int(input())

R_convert = [x for x in R]
C_convert = [x for x in C]
ans = ''

for i in range(Q):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    if R_convert[r]+C_convert[c] > N-2:
        ans += '#'
    else:
        ans += '.'

print(ans)
