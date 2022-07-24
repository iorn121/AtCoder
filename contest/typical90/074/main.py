N= int(input())
S=input()

ans=0
for i in range(N):
    if S[i]=="b":
        ans+=(2**i)*1
    elif S[i]=="c":
        ans+=(2**i)*2
print(ans)