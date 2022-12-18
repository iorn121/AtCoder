N=int(input())
H=list(map(int, input().split()))
m=max(H)
for i,h in enumerate(H,1):
    if h==m:
        exit(print(i))