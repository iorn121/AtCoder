X = input()
convert = {}
for i in range(26):
    convert[X[i]] = chr(97+i)
N = int(input())

S = []
ans = []
for i in range(N):
    s = input()
    ans.append(s)
    news = ""
    for j in range(len(s)):
        news += convert[s[j]]
    S.append((news, i))

S.sort()

for i in range(N):
    n = S[i][1]
    print(ans[n])
