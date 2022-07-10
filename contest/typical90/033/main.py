H, W = map(int, input().split())
if H == 1 or W == 1:
    exit(print(H*W))
print(((H+1)//2)*((W+1)//2))
