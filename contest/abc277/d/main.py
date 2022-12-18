N,M = map(int, input().split())
A= list(map(int, input().split()))

cnt=[0]*M
total=sum(A)
check=set(A)
for a in A:
    cnt[a]+=1

check2=[]
tmp=0
for c in check:
    tmp+=c*cnt[c]
    if c+1 not in check:
        check2.append(tmp)
        tmp=0
if len(check2)==1:
    exit(print(0))
if 0 in check and M-1 in check:
    check2[0]+=check2[-1]
    check2[-1]=0

# print(check2)


print(total-max(check2))