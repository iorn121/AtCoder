from collections import Counter

N, K = map(int, input().split())
cnt = 0
A = list(map(int, input().split()))
A.sort(reverse=True)
AA=A[:K]
BB=A[K:]
while Counter(AA)[0]!=0 and BB ==[]:
    x=min(AA)
    cnt += x
    AA=[i-x for i in AA]
    

print(cnt)
