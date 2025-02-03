X=int(input())
cnt=0
for i in range(1, 10):
    if X%i!=0:
        continue
    if X//i<=9:
        cnt+=1
print(2025-X*cnt)