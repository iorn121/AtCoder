A=list(map(int,input().split()))
cnt=[]
for i,a in enumerate(A,1):
    if a!=i:
        cnt.append(i)

print("Yes" if len(cnt)==2 and cnt[0]+1 == cnt[1] else "No")