S= input()
T= input()
if len(S)>len(T):
    exit(print("No"))

nT=T[:len(S)]
for s,t in zip(S,nT):
    if s!=t:
        exit(print("No"))
print("Yes")