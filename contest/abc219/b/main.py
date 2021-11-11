S = []
for i in range(3):
    S.append(input())

T = input()
ans = ""
for i in range(len(T)):
    ans += S[int(T[i])-1]

print(ans)
