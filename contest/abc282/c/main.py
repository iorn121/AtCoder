N= int(input())
S=list(input())

cnt=0
ans=S[:]
for i,s in enumerate(S):
    if s=="\"":
        cnt+=1
    elif s=="," and cnt%2==0:
        ans[i]="."

print("".join(ans))