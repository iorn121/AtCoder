X=int(input())

one_list=[0]
for i in range(61):
    if (X>>i)&1:
        one_list.append(2**i)
N=len(one_list)
check=set()
for i in range(1<<N):
    ans=0
    for j in range(N):
        if (i>>j)&1:
            ans+=one_list[j]
    if ans not in check:
        print(ans)
        check.add(ans)