T=int(input())

for _ in range(T):
    N,K= map(int, input().split())
    S= list(input())
    check=-1
    flg=True
    cnt=0
    for i in range(K):
        if S[i]!="0":
            cnt+=1
    if cnt==K:
        check=0
    for i in range(N-K):
        if check>0:
            break
        if S[i]!="0":
            cnt-=1
        if S[i+K]!="0":
            cnt+=1
        if cnt==K:
            check=i+1
    if check==-1:
        print("No")
        continue
    for i,s in enumerate(S):
        if check<=i<check+K and s[i]!="0":
            
    print(check)

    print("Yes" if sum(check)==1 else "No")