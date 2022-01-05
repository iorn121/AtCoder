L, R = map(int, input().split())
L -= 1
S = input()
rev = S[L:R]
ans = S[:L]+rev[::-1]+S[R:]
print(ans)
