N=int(input())
A=list(map(int, input().split()))
ans=0
for center in range(N):
    a=A[center]
    if center-a<0:
        continue
    if center+a>=N:
        continue