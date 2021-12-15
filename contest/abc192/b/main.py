S = input()
N = len(S)
flg = True
for i in range(1, N, 2):
    if S[i].islower():
        flg = False
for i in range(0, N, 2):
    if S[i].isupper():
        flg = False
print("Yes" if flg else "No")
