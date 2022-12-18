N,M = map(int, input().split())
s=[set() for _ in range(N)]
for i in range(M):
    p=list(map(int, input().split()))
    for j in p[1:]:
        s[j-1].add(i)

flg=True
for i in range(N-1):
    for j in range(i+1, N):
        if not s[i]&s[j]:
            flg=False

print("Yes" if flg else "No")