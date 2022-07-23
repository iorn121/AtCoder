L1,R1,L2,R2= map(int, input().split())

minR=min(R1,R2)
maxL=max(L1,L2)
print(max(0,minR-maxL))