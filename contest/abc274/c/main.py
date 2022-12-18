N= int(input())
A=list(map(int, input().split()))
num=[0]*(2*N+2)
for i,a in enumerate(A,1):
    c=num[a]
    num[2*i]=c+1
    num[2*i+1]=c+1
    # print(num)
for n in num[1:]:
    print(n)