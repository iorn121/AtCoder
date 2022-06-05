N= int(input())

check=[0]*(N+1)

for i in range(1,N+1):
    if check[i]!=0:
        continue
    j=1
    tmp=0
    cnt=[]
    while i*j*j<=N:
        cnt.append(i*j*j)
        tmp+=1
        j+=1
    for c in cnt:
        check[c]=tmp
print(sum(check))