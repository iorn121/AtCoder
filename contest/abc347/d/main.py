a,b,C=map(int,input().split())
c_popcount=bin(C).count('1')
c_digits=len(bin(C)[2:])
c_zero=c_digits-c_popcount
if a+b<c_popcount or (a+b-c_popcount)%2==1:
    print(-1)
    exit()
zero=min((a+b-c_popcount)//2,c_zero)
head=max(0,(a+b-c_popcount)//2-c_zero)
a-=zero+head
b-=zero+head
if a<0 or b<0:
    print(-1)
    exit()
A=0
B=0
cnt=0
zero_cnt=0
for i in range(c_digits):
    if C&(1<<i):
        if cnt<a:
            A+=2**i
        else:
            B+=2**i
        cnt+=1
    else:
        if zero_cnt<zero:
            A+=2**i
            B+=2**i
            zero_cnt+=1
# print(c_popcount,c_digits,c_zero,zero,head,A,B)
if head>0:
    for i in range(c_digits,c_digits+head):
        A+=2**i
        B+=2**i
if A>=2**60 or B>=2**60:
    print(-1)
    exit()
print(A,B)