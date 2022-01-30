S = input()
N = len(S)
cnt = 0
for i in range(N-1, -1, -1):
    if S[i] == 'a':
        cnt += 1
    else:
        break
c = 0
for i in range(N):
    if S[i] == 'a':
        c += 1
    else:
        break
flg = False
newS = 'a'*(cnt-c)+S
if newS == newS[::-1]:
    flg = True
print('Yes' if flg else 'No')
