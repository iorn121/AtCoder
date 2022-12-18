N= int(input())
A=list(map(int, input().split()))

odd=[]
even=[]
for a in A:
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)

if len(odd)<2 and len(even)<2:
    exit(print(-1))

ans=0
odd.sort(reverse=True)
even.sort(reverse=True)
if len(odd)>=2:
    ans=max(ans,odd[0]+odd[1])
if len(even)>=2:
    ans=max(ans,even[0]+even[1])
print(ans)