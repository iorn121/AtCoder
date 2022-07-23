N= int(input())
A=list(map(int, input().split()))

total=sum(A)
if total%10!=0:
    exit(print("No"))
goal=total//10
A=A*2
count=0
start=0
for i in range(2*N):
    count+=A[i]
    if count==goal:
        exit(print("Yes"))
    while count>goal:
        count-=A[start]
        start+=1
print("No")