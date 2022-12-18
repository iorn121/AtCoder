H,W= map(int, input().split())
S=[list(input()) for _ in range(H)]
T=[list(input()) for _ in range(H)]
tS=list(zip(*S))
tT=list(zip(*T))
tS.sort()
tT.sort()
if tS==tT:
    print("Yes")
else:
    print("No")
