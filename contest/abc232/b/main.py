S = input()
T = input()
convertS = []
convertT = []
s = ord(S[0])
t = ord(T[0])
for i in range(len(S)):
    ss = ord(S[i])-s
    tt = ord(T[i])-t
    if ss < 0:
        ss += 26
    if tt < 0:
        tt += 26
    convertS.append(ss)
    convertT.append(tt)

if convertS == convertT:
    print("Yes")
else:
    print("No")
