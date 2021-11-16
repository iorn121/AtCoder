N = int(input())
s = set()
for i in range(N):
    S, T = input().split()
    newS = S+" "+T
    s.add(newS)

print("Yes" if len(s) != N else "No")
