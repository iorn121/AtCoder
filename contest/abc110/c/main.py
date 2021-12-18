S = input()
T = input()
N = len(S)
check1 = [[] for _ in range(26)]
check2 = [[] for _ in range(26)]
for i in range(N):
    s = ord(S[i])-97
    t = ord(T[i])-97
    if t not in check1[s]:
        check1[s].append(t)
    if s not in check2[t]:
        check2[t].append(s)

flg = True
for i in range(26):
    if len(check1[i]) > 1:
        flg = False
    if len(check2[i]) > 1:
        flg = False

print("Yes" if flg else "No")
