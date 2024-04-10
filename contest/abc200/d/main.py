# N=int(input())
# A=list(map(int,input().split()))[:8]

# sum_dict={}
# for a in range(1,1<<len(A)):
#     ids=[i+1 for i in range(len(A)) if a & 1<<i]
#     ans=sum([A[i] for i in range(len(A)) if a & 1<<i])%200
#     if ans in sum_dict:
#         print("Yes")
#         print(len(sum_dict[ans]),*sum_dict[ans])
#         print(len(ids),*ids)
#         exit()
#     else:
#         sum_dict[ans]=ids

import collections
N=int(input())
A=list(map(int,input().split()))

sum_dict=collections.defaultdict(list)
dp=[False]*200
dp[0]=True
for i,a in enumerate(A,1):
    ndp=dp[:]
    for j in range(200):
        if j==0 and sum_dict[j]!=[]:
            print("Yes")
            print(len(sum_dict[j])+1,*sum_dict[j],i)
            print(1,i)
            exit()
        if not dp[j]:
            continue
        next_j=(j+a)%200
        if next_j in sum_dict and sum_dict[next_j]!=[]:
            print("Yes")
            print(len(sum_dict[next_j]),*sum_dict[next_j])
            print(len(sum_dict[j])+1,*sum_dict[j],i)
            exit()
        sum_dict[next_j]=sum_dict[j][:]+[i]
        ndp[next_j]=True
    dp=ndp[:]
    # print(sum_dict)
# print(len(sum_dict))

print("No")