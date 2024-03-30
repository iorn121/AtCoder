N,A,B=map(int,input().split())
D=list(map(int,input().split()))
new_D=[d%(A+B) for d in D]
new_D.sort()
flg=False
# print(new_D)
for i in range(N):
    start=new_D[i]
    end=start+A
    # print(start,end)
    if i==0:
        if new_D[-1]<end:
            flg=True
            break
    else:
        if new_D[i-1]+A+B<end:
            flg=True
            break
print('Yes' if flg else 'No')