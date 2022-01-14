S = input().replace('25', 'X')
N = len(S)
ans = 0


def wa(x):
    return x*(x+1)//2


seq = 0
for s in S:
    if s == 'X':
        seq += 1
    else:
        ans += wa(seq)
        seq = 0
ans += wa(seq)
print(ans)
