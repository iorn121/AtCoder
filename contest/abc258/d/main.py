N, X = map(int, input().split())
AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))

base = sum(AB[0])
check = base+AB[0][1]*(X-1)
for i in range(min(X-1,N-1)):
    base += sum(AB[i+1])
    total = base+AB[i+1][1]*(X-i-2)
    check = min(check, total)
print(check)
