S= list(input())
convert=[3,2,4,1,3,5,0,2,4,6]
check=[False]*7
for i,s in enumerate(S):
    if i==0 and s=="1":
        exit(print("No"))
    if s=="1":
        check[convert[i]]=True
cnt=0
for i in range(6):
    if check[i] and not check[i+1]:
        cnt+=1
        
    elif cnt>0 and not check[i] and check[i+1]:
        cnt+=1
# print(check)
# print(cnt)
print("Yes" if cnt>=2 else "No")