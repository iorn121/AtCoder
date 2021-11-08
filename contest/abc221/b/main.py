from itertools import permutations

flg = False
S = list(input())
T = list(input())
if S == T:
    flg = True
for i in range(len(S)-1):
    SS = S[:]
    SS[i], SS[i+1] = SS[i+1], SS[i]
    if(SS == T):
        flg = True

print("Yes" if flg else "No")
