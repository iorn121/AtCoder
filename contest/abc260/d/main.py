N,K= map(int, input().split())
P= list(map(int, input().split()))

field=[]
ans=[-1]*N
for i,p in enumerate(P):
    p-=1
    pos=0
    if field==[]:
        field.append([p])
    elif field[-1][0]<p:
        field.append([p])
    else:
        left=-1
        right=len(field)+1
        while left+1<right:
            mid = (left+right)//2
            if field[mid][-1]>=p:
                right=mid
            else:
                left=mid
        field[right].append(p)
        pos=right
    # print(field)
    if len(field[pos])>=K:
        # print(field[pos])
        for x in field[pos]:
            ans[x]=i+1
        del field[pos]

for i in ans:
    print(i)
    