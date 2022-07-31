N= int(input())
A=list(map(int, input().split()))

even=0
cross=0
for i,a in enumerate(A,1):
    if i==a:
        even+=1
    elif A[a-1]==i:
        cross+=1

print(even*(even-1)//2+cross//2)