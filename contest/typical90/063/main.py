from collections import defaultdict
H,W=map(int, input().split())
P=[list(map(int, input().split())) for i in range(H)]
ans=0
same_col_list=[defaultdict(int) for _ in range(1<<H)]
col_point=[0]*(1<<H)
for i in range(1<<H):
    cnt=0
    for j in range(H):
        if (i>>j)&1:
            cnt+=1
    col_point[i]=cnt
for col in range(W):
    for i in range(1<<H):
        int_set=set()
        for j in range(H):
            if (i>>j)&1:
                int_set.add(P[j][col])
        if len(int_set)==1:
            s=int_set.pop()
            same_col_list[i][s] +=1
import pprint
for i in range(1<<H):
    # print(col_point[i])
    if same_col_list[i]:
        # pprint.pprint(max(same_col_list[i]))
        ans=max(ans,col_point[i]*max(same_col_list[i].values()))

print(ans)