N, K, X = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
cnt = 0
newA = []
for a in A:
    cnt += a//X
    newA.append(a % X)
# print(len(newA))
newA.sort(reverse=True)
# print(newA)

if K <= cnt:
    print(total-K*X)
elif K >= cnt+N:
    print(0)
else:
    print(total-cnt*X-sum(newA[0:K-cnt]))
