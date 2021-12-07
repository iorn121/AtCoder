S = input()
S = S[::-1]
N = len(S)
ans = ""

for i in range(N):
    if S[i] == "6":
        ans += "9"
    elif S[i] == "9":
        ans += "6"
    else:
        ans += S[i]

print(ans)
